import pygame
import time
import datetime

alarmfile = '0788.wav'
file = alarmfile
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
