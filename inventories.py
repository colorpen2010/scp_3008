import pygame,settings
class Inventory_system:
    def __init__(self,visib):
        self.visib=visib
        self.rect=pygame.rect.Rect(0,0,settings.SIZE[0]-100,settings.SIZE[1]-100)
    def risovanie(self,screen:pygame.Surface):
        inventory=pygame.Surface([settings.SIZE[0]-100,settings.SIZE[1]-100],pygame.SRCALPHA)
        inventory.fill([255,0,0])
        pygame.draw.rect(inventory,[50,50,50,200],self.rect,border_radius=10)
        if self.visib==True:
            screen.blit(inventory,[50,50])