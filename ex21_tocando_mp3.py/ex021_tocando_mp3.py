import pygame

pygame.mixer.init()
pygame.mixer.music.load('musicapy.mp3')
pygame.mixer.music.play()
pygame.event.wait()
