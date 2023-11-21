import pygame,model, settings
pygame.init()
screen=pygame.display.set_mode(settings.SIZE)
pygame.mixer_music.load('audio/music/friday_theme.mp3')
# pygame.mixer_music.set_volume(0.1)
# pygame.mixer_music.play(-1)
def risovanie():
    screen.fill([0,0,0])
    model.box1.risyem(screen)
    model.player.risyem(screen)
    model.water.risyem(screen)
    model.inventory.risovanie(screen)
    if settings.debug_mode==True:
        pygame.draw.rect(screen,[35,234,20],model.pickup,3)
    pygame.display.flip()
