# Faça um programa em python que abra e reproduza o audio de um arquivo mp3

# Importa o módulo pygame para manipulação de áudio
import pygame

# Inicializa o pygame
pygame.init()

# Inicializa o mixer do pygame, responsável pelo áudio
pygame.mixer.init()

# Carrega o arquivo de áudio MP3 especificado
pygame.mixer.music.load('exe021.mp3')

# Reproduz o arquivo de áudio carregado
pygame.mixer.music.play()

# Mantém o programa em execução enquanto o áudio está sendo reproduzido
pygame.event.wait()

