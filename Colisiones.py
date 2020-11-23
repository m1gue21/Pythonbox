import pygame, random,sys
pygame.init()

#colores
black = ( 0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

score = 0

#definicion de clases
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


#tamaño pantalla
screen_size = (900, 600)


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

game_over =  False
while not game_over:
    for event in pygame.event.get():
         #CERRAR VENTANA SIN PROBLEMAS 
        if event.type == pygame.QUIT:
            game_over = True
    mouse_pos = pygame.mouse.get_pos() 
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]
    pygame.mouse.set_visible(0)

    for meteor in meteor_list:
        meteor.rect.y += 1
        if meteor.rect.y > 600:
            meteor.rect.y = 0
            meteor.rect.x = random.randrange(900)

    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    for meteor in meteor_hit_list:
        score += 1
        print(score)
    

   



    screen.fill(white)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()