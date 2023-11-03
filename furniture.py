import pygame
class Furniture:
    def __init__(self,bX,bY,player,pyt_k_kartinke):
        self.bY = bY
        self.bX=bX
        self.player=player
        self.mebel = pygame.image.load(pyt_k_kartinke)
    def risyem(self,screen:pygame.Surface):
        screen.blit(self.mebel,[self.bX-self.player.bX+400,self.bY-self.player.bY+400])
