import pygame,model
pygame.key.set_repeat(100)
def control():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_w:
            model.pmoveY-=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_s:
            model.pmoveY+=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_a:
            model.pmoveX-=25
        if o.type == pygame.KEYDOWN and o.key == pygame.K_d:
            model.pmoveX+=25