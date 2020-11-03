import pygame, sys

pygame.init()

#COLORES
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 500) 

#crear ventana
screen = pygame.display.set_mode(size)
#controlar el tiempo(fps del juego)
clock = pygame.time.Clock()
#coordenadas
cord_x = 63
cord_y = 27

#velocidad del cuadrado
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get(): #registrar o identificar lo que sucede en la ventana 
        if event.type == pygame.QUIT:
            sys.exitÇ() #HERRAMIENTA PARA PODER CERRAR LA PESTAÑA DEL JUEGO
    
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x 
    cord_y += speed_y

    #color de fondo
    screen.fill(WHITE)
    #ZONA DE DIBUJO#
    pygame.draw.rect(screen, BLUE, (cord_x, cord_y, 80, 80))

    #ZONA DE DIBUJO#
    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)