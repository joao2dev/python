import pygame

pygame.init()
file = 'home.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.time.delay(500000)
pygame.mixer.music.stop()


