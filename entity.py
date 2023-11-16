import pygame, settings

import model


class Entity:
    def __init__(self, bX, bY, player, pyt_k_kartinke):
        self.bY = bY
        self.bX = bX
        self.player = player
        self.mebel = pygame.image.load(pyt_k_kartinke)

    def risyem(self, screen: pygame.Surface):
        rect = pygame.rect.Rect(20, 20, self.mebel.get_width(), self.mebel.get_height())
        rect.centerx = self.bX - self.player.bX + settings.SIZE[0] / 2
        rect.centery = self.bY - self.player.bY + settings.SIZE[1] / 2
        screen.blit(self.mebel, rect)
        pygame.draw.rect(screen,[35,234,20],rect,3)
