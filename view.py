import pygame,model

screen=pygame.display.set_mode([800,800])
def risovanie():
    box2=model.box
    player2=model.player
    screen.fill([0,0,0])
    screen.blit(player2,[400,400])
    screen.blit(box2,[model.bmoveX-model.pmoveX+400,model.bmoveY-model.pmoveY+400])
    pygame.display.flip()