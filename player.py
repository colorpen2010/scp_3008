import pygame, entity, settings,backfiles


class Player(entity.Entity):
    def __init__(self):
        entity.Entity.__init__(self, 200, 200, None, 'sprites/player/игрок2.png')
        backfiles.player = self
        self.player = self

        self.pickup = pygame.rect.Rect(self.bX, self.bY, 100, 100)

    def risyem(self, screen: pygame.Surface):
        self.nrect=pygame.rect.Rect(self.bX, self.bY, 100, 100)
        self.nrect.x = backfiles.xmovier(self.pickup.x)
        self.nrect.y = backfiles.ymovier(self.pickup.y)
        entity.Entity.risyem(self, screen)
        if settings.debug_mode:
            pygame.draw.rect(screen, [0, 200, 0], self.nrect, 3)

    def moveup(self):
        self.bY -= 25
        self.pickup.y = self.bY - 80
        self.pickup.x = self.bX - 42

    def movedown(self):
        self.bY += 25
        self.pickup.y = self.bY + 30
        self.pickup.x = self.bX - 42

    def moveleft(self):
        self.bX -= 25
        self.pickup.x = self.bX + 0
        self.pickup.y = self.bY - 25


    def moveright(self):
        self.bX += 25
        self.pickup.x = self.bX-80
        self.pickup.y = self.bY - 25

