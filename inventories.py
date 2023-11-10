import pygame,settings
class Inventory_system:
    def __init__(self):
        self.rect=pygame.rect.Rect(100,100,settings.SIZE[0]-200,settings.SIZE[1]-200)
    def risovanie(self,screen:pygame.Surface):
        inventory=pygame.Surface([settings.SIZE[0]-200,settings.SIZE[1]-200],pygame.SRCALPHA)
        inventory.fill([255,0,0])
        pygame.draw.rect(inventory,[50,50,50,200],self.rect,border_radius=10)
        screen.blit(inventory,[40,50])