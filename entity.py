import pygame, settings

def xmovier(player,bX):
    return bX - player.bX + settings.SIZE[0] / 2
def ymovier(player,bY):
    return bY - player.bY + settings.SIZE[1] / 2


class Entity:
    def __init__(self, bX, bY, player, pyt_k_kartinke):
        self.bY = bY
        self.bX = bX
        self.player = player
        if player==None:
            self.player=self
        self.mebel = pygame.image.load(pyt_k_kartinke)


    def risyem(self, screen: pygame.Surface):
        rect = pygame.rect.Rect(20, 20, self.mebel.get_width(), self.mebel.get_height())
        rect.x = xmovier(self.player,self.bX)
        rect.y = ymovier(self.player,self.bY)
        screen.blit(self.mebel, rect)
        if settings.debug_mode==True:
            pygame.draw.rect(screen,[35,234,20],rect,3)
