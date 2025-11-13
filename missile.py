import pygame
from constants import *
missile_image = pygame.image.load('images/missile.png')

def create_missile(x,y):
    tmp_image = pygame.transform.scale(missile_image, (WALL_DX/2,WALL_DY/2))
    surf = tmp_image.convert_alpha()
    surf.set_colorkey((255, 255, 255))  # Rende il bianco trasparente
    rect = surf.get_rect()
    rect.left = x
    rect.top = y
    return {"surf": surf, "rect": rect}

def update_missile(missile):
    missile["rect"].move_ip(5,0)
    # Rimuovi il missile se esce dallo schermo
    if missile["rect"].left > SCREEN_WIDTH:
        return False
    return True
