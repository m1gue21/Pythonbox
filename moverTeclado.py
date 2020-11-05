import pygame, sys
pygame.init()

black = ( 0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

size = (800, 500) 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

#COORD DEL OBJETO
coord_x = 10
coord_y = 300

#velocidad
x_speed = 0 
y_speed = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exitÇ() 
        #conf del teclado 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    screen.fill(white)

    coord_x += x_speed
    coord_y += y_speed

    #OBJETOS
    pygame.draw.rect(screen, red, (coord_x, coord_y, 100,100))
    #OBJETOS
    pygame.display.flip()
    clock.tick(60)