import pygame
from settings import *
from playerdebug import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect(topleft=pos)

        #graphics setup
        self.import_player_assets
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
# 15/09/2024
    def import_player_assets(self):
        character_path = '../'
        self.animations = {'up':['R.png', 'R2.png', 'R3.png', 'R4.png', 'R3.png', 'R2.png'],
                           'down':['R.png', 'R2.png', 'R3.png', 'R4.png', 'R3.png', 'R2.png'],
                           'left':['L.png', 'L2.png', 'L3.png', 'L4.png', 'L5.png', 'L4.png', 'L3.png', 'L2.png',],
                           'right':['R.png', 'R2.png', 'R3.png', 'R4.png', 'R3.png', 'R2.png'],
                           }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation]
            print(animation)


    def animate(self):
        animation = self.animations[self.status]
        #loop frame index
        self.frame_index += self.animation_speed
        
        #image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
 #end
        #self.obstacle_sprites = obstacle_sprites
    # Player settings
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    player_pos = [100,100]
    safe_position = [WIDTH // 2, HEIGHT // 2]  # Safe position within the map

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0



    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        #self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #self.collision('vertical')

        if self.rect.left < 0  : # checking the left side screen
            self.rect.left = 0 # setting the left side screen
        if self.rect.right > WIDTH: # checking the right side screen
            self.rect.right = WIDTH # setting the right side screen
        if self.rect.top <= 0: # checking the up
            self.rect.top = 0 # setting the up
        if self.rect.bottom >= HEIGHT: # checking the base
            self.rect.bottom = HEIGHT # setting the base

    #def collision(self, direction):
                    #if direction == 'horizontal':                  
#for sprite in self.obstacle_sprites:
                #if self.rect.colliderect(sprite.rect):
                    #if self.direction.x > 0:  # moving right
                        #self.rect.right = sprite.rect.left
                    #if self.direction.x < 0:  # moving left
                        #self.rect.left = sprite.rect.right
        #if direction == 'vertical':
            #for sprite in #self.obstacle_sprites:
                #if self.rect.colliderect(sprite.rect):
                    #if self.direction.y > 0:  # moving down
                        #self.rect.bottom = sprite.rect.top
                    #if self.direction.y < 0:  # moving up
                        #self.rect.top = sprite.rect.bottom
    def update(self):
        self.input()
        self.animate
        self.move(self.speed)