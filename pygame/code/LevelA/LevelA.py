import pygame
import sys
pygame.init()


#game windw
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('LevelA')


#set framerate
clock = pygame.time.Clock()
FPS = 60
#load images

background_img = pygame.image.load('levelwall.png').convert_alpha()


#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  #player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#func for background
def draw_bg():
    scaled_bg = pygame.transform.scale(background_img, (screen_width, screen_height))
    screen.blit(scaled_bg,(0, 0))

     #update display
    #pygame.display.update()


class Fighter:
    def __init__(self, x, y,image):
        self.image = pygame.image.load('stanceA.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.health = 100
        self.alive = True

    def move(self):
        SPEED = 10
        dx = 0
        dy = 0
        #keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
         dx = -SPEED
        elif key[pygame.K_d]:
         dx = SPEED
            #Player pos
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def update(self):
        if self.health <= 0:
            self.alive = False

         #creating fighter instance
Fighter1 = Fighter(100, 300, 'stanceA.png')
Fighter2 = Fighter(600, 300, 'zeus.png')  # image path

if Fighter1.rect.colliderect(Fighter2.rect):
    print('collision detected')

class Player(pygame.sprite.Sprite):
    # Other

     def draw(self, surface):
       pygame.draw.rect(surface, self.COLOR, self.rect)


    # health bars
       health_bar1.draw(screen)
       health_bar2.draw(screen)

    #check player defeat
if round_over == False:
      if not Fighter1.alive:
       score[1] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()
elif Fighter2.alive == False:
      score[0] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()

def handle_movement(keys, fighter):
    if keys[pygame.K_LEFT]:
        fighter.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        fighter.rect.x += 5
    if keys[pygame.K_UP]:
        fighter.rect.y -= 5
    if keys[pygame.K_DOWN]:
        fighter.rect.y += 5

def check_collision(fighter1, fighter2):
    return fighter1.rect.colliderect(fighter2.rect)

def attack(fighter1, fighter2):
    if check_collision(fighter1, fighter2):
        print("Attack")

    
    #2nd main loop
    if check_collision(fighter1, fighter2):
        attack (fighter1, fighter2)
    clock.tick(FPS)
class Healthbar:
    def __init__(self, x,y, health):
        self.health = health
        self.rect = pygame.Rect(x, y, 100, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), 
                         self.rect)
        pygame.draw.rect(surface, (0, 255, 0), 
                         (self.rect.x, self.rect.y, self.health, 
                          self.rect.height))

        # create health bars
health_bar1 = Healthbar(100, 50, 100)
health_bar2 = Healthbar(600, 50, 100)

health_bar1.draw(screen)
health_bar2.draw(screen)

Fighter1.health -= 100

draw_bg()

clock.tick(FPS)


run = True
while run:
    clock.tick(FPS)
    draw_bg
    Fighter1.update()
    Fighter2.update()
    Fighter1.draw(screen)
    Fighter2.draw(screen)
    pygame.display.update()

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Handle movement
keys = pygame.key.get_pressed()
handle_movement(keys, Fighter1)
handle_movement(keys, Fighter2)

   #collisions and handle attacks
if check_collision(Fighter1, Fighter2):
   attack(Fighter1, Fighter2)  # Implement attack

#create two instances of fighters
#Fighter1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
#Fighter2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)




  #show player stats
  #draw_health_bar(fighter_1.health, 20, 20)
  #draw_health_bar(fighter_2.health, 580, 20)
  #draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
  #draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)









