# abra e reproduza um audio arquivo em mp3
import pygame
pygame.init()
pygame.mixer.music.load('wkm.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())