import pygame,model
pygame.key.set_repeat(100)
def control():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            return
        if o.type == pygame.KEYDOWN and o.key == pygame.K_w:
            model.player.bY-=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_s:
            model.player.bY+=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_a:
            model.player.bX-=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_d:
            model.player.bX+=25