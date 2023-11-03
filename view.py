import pygame,model

screen=pygame.display.set_mode([800,800])
def risovanie():
    screen.fill([0,0,0])
    model.box1.risyem(screen)
    model.player2.risyem(screen)
    pygame.display.flip()