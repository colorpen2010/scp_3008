import pygame, model

import settings

pygame.key.set_repeat(100)


def control():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            return
        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            settings.debug_mode = not settings.debug_mode
        if o.type == pygame.KEYDOWN and o.key == pygame.K_w:
            model.player.moveup()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_s:
            model.player.movedown()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_a:
            model.player.moveleft()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_d:
            model.player.moveright()
        if o.type == pygame.KEYUP and o.key == pygame.K_e:
            model.inventory.visib = not model.inventory.visib
