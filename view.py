import pygame,model

screen=pygame.display.set_mode([800,800])
def risovanie():
    screen.blit(model.player,[400,400])
    screen.blit(model.box,[450,450])
    pygame.display.flip()