# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3.

# O codigo foi atualizado, o pessoal pelo youtube nos comentários dessa aula informaram que
# deveria ser acrescentado o input(), como eu fiz abaixo!

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
