import pygame, entity, settings


class Player(entity.Entity):
    def __init__(self):
        entity.Entity.__init__(self, 200, 200, None, 'sprites/player/игрок.png')
        self.player = self

        self.pickup = pygame.rect.Rect(self.bX, self.bY, 100, 100)
        self.pickup.centerx = self.bX - self.player.bX + settings.SIZE[0] / 2
        self.pickup.centery = self.bY - self.player.bY + settings.SIZE[1] / 2

    def risyem(self, screen: pygame.Surface):
        entity.Entity.risyem(self, screen)
        if settings.debug_mode:
            pygame.draw.rect(screen, [0, 200, 0], self.pickup, 3)

    def moveup(self):
        self.bY -= 25
        # self.pickup.centery=

    def movedown(self):
        self.bY += 25

    def moveleft(self):
        self.bX -= 25

    def moveright(self):
        self.bX += 25
