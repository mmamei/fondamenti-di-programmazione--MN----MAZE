import pygame
from constants import *
missile_image = pygame.image.load('images/missile.png')
missile_image = pygame.transform.scale(missile_image, (WALL_DX/2,WALL_DY/2))

def create_missile(x,y, direction):
    surf = pygame.transform.rotate(missile_image, direction - 90)
    surf = surf.convert_alpha()
    surf.set_colorkey((255, 255, 255))  # Rende il bianco trasparente
    rect = surf.get_rect()
    rect.centerx = x
    rect.centery = y

    dx = 0
    dy = 0
    if direction == 0:  # Down
        dy = 5
    elif direction == 90:  # Right
        dx = 5
    elif direction == 180:  # Up
        dy = -5
    elif direction == 270:  # Left
        dx = -5
    
    return {"surf": surf, "rect": rect, 'dx':dx, 'dy':dy}

def update_missile(missile, wall_list):
    missile["rect"].move_ip(missile['dx'], missile['dy'])
    
    # Rimuovi il missile se esce dallo schermo
    if (missile["rect"].left > SCREEN_WIDTH or missile["rect"].right < 0 or
        missile["rect"].top > SCREEN_HEIGHT or missile["rect"].bottom < 0):
        return True
    
    # Wall collision
    for wall in wall_list:
        if missile["rect"].colliderect(wall["rect"]):
            return True
    
    return False
