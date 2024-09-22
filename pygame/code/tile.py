import pygame
# from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(250,250))
        self.rect = self.image.get_rect(topleft = pos)
        









        