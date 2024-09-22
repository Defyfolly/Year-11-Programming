import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
import LevelA

class Level:
    def __init__(self) -> None:
        # Getting display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #Create prtal hitbx in right up
        portal_width = 100
        portal_height = 100
        portal_x = WIDTH - portal_width
        portal_y = 0
        portal_hitbox = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
        self.portal.hitbox = portal_hitbox
        

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                #if col == 'x':
                   # Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Updating and drawing the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)

#portal collision
        if self.player.rect.colliderect(self.portal_hitbox):
            print("Portal")
            self.load_level('LevelA')

    def load_level(self, level_name):
        if level_name == 'LevelA':
            LevelA.run_level_A()

class YCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Creating the floor
        self.floor_surface = pygame.image.load('tilemap.png').convert_alpha()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # Getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        # Draw all sprites with the offset
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

# added border 

