import pygame
class Inventory_system:
    def __init__(self):
        self.rect=pygame.rect.Rect(100,100,600,600)
    def risovanie(self,screen:pygame.Surface):
        inventory=pygame.Surface([700,600],pygame.SRCALPHA)
        pygame.draw.rect(inventory,[50,50,50,200],self.rect,border_radius=10)
        screen.blit(inventory,[40,50])