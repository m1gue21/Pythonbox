import pygame
pygame.init()

#colores
black = ( 0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


#tamaño pantalla
screen_size = (800, 600)
#tamaño jugadores
player_width= 15
player_height= 90
#coordenadas y velocidad jugador1
player1_x_coord = 50
player1_y_coord = 300 - 45
player1_y_speed = 0
#coordenadas y velocidad jugador2
player2_x_coord = 750 - player_width
player2_y_coord = 300 - 45
player2_y_speed = 0
#coordenadas balon
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_over =  False

while not game_over:
    for event in pygame.event.get():
         #CERRAR VENTANA SIN PROBLEMAS 
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN: #presionar tecla
            #jugador1
            if event.key == pygame.K_w:
                player1_y_speed = -3 
            if event.key == pygame.K_s:
                player1_y_speed = 3 
            #jugador2
            if event.key == pygame.K_UP:
                player2_y_speed = -3 
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
        if event.type == pygame.KEYUP:#soltar tecla 
            #jugador1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #jugador
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0


    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y*= -1
    # si la pelota sale #
    #DERECHA
    if pelota_x > 800: # hace que la pelota vuelva a su posicion original
        pelota_x = 400
        pelota_y = 300
        # hace que la pelota salga hacia el lado contrario 
        pelota_speed_x *= -1
        pelota_speed_y *= -1 
    #IZQUIERDA 
    if pelota_x < 0: # hace que la pelota vuelva a su posicion original
        pelota_x = 400
        pelota_y = 300
        # hace que la pelota salga hacia el lado contrario 
        pelota_speed_x *= -1
        pelota_speed_y *= -1 
    #movimientos jugadores
    player1_y_coord += player1_y_speed
    player2_y_coord += player2_y_speed
    #movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y


    

    screen.fill(black)
    #dibujos
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coord, player1_y_coord, player_width, player_height))
    jugador2 =pygame.draw.rect(screen, white, (player2_x_coord, player2_y_coord, player_width, player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

    # hacer que la pelota rebote en los jugadores 
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
