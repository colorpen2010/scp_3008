import pygame,model
pygame.init()
screen=pygame.display.set_mode([800,800])
pygame.mixer_music.load('audio/music/friday_theme.mp3')
pygame.mixer_music.set_volume(0.1)
pygame.mixer_music.play(-1)
def risovanie():
    screen.fill([0,0,0])
    model.box1.risyem(screen)
    model.player.risyem(screen)
    model.inventory.risovanie(screen)
    pygame.display.flip()
