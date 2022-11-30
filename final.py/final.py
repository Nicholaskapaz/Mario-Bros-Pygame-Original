# Importando as bibliotecas 
import pygame
import random
from classes import *
from os import path
from pygame import mixer 

def inicializa_jogo():
    
    pygame.init()
    mixer.init()

    # Tela principal 
    titulo = 'SUPER MACIEL BROS'
    width = 1200 #largura da tela 
    height = 390 #altura da tela 
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption('SUPER MACIEL BROS')
    title_size = 100 #tamanho de cada titulo 
    FPS = 30
    w_m = 75
    h_m = 90
    w_p = 60
    h_p = 75
    x = 0 
    y = 0
    
    # Definindo assets
    assets = {}
    assets['mapa'] = pygame.image.load('sprite/fundo_pygame.png').convert_alpha()
    assets['mapa'] = pygame.transform.scale(assets['mapa'],(width,height)) 
    assets['personagem_maciel'] = pygame.image.load('sprite/personagem_maciel.png').convert_alpha()
    assets['personagem_maciel'] = pygame.transform.scale(assets['personagem_maciel'],(w_m,h_m))
    assets['maciel_pulando'] = pygame.image.load('sprite/maciel_pulando_png.png').convert_alpha()
    assets['maciel_pulando'] = pygame.transform.scale(assets['maciel_pulando'],(w_m,h_m))
    assets['pedra'] = pygame.image.load('sprite/pedra.png').convert_alpha()
    assets['pedra'] = pygame.transform.scale(assets['pedra'],(w_p,h_p))
    assets['leao'] = pygame.image.load('sprite/leao.png').convert_alpha()
    assets['leao'] = pygame.transform.scale(assets['leao'],(w_p+30,h_p+10))
    assets['caveira'] = pygame.image.load('sprite/caveira.png').convert_alpha()
    assets['caveira'] = pygame.transform.scale(assets['caveira'],(69,69))
    assets['coracao'] = pygame.image.load('sprite/heart.png').convert_alpha()
    assets['coracao'] = pygame.transform.scale(assets['coracao'],(69,69))
    assets['fonte_50'] = pygame.font.Font('Fontes/ARCADE.ttf', 50)

 # Carrega os sons do jogo
    
    mixer.music.load('biblioteca.py\musica_pygame.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()

# mixer.music.load()

    state = {
        'acabou': False,
        'maciel_pos': [50,216],
        'maciel_speed': [0,0],
        'gravidade': 100,
        'pulando': False,
        'time_update': 0,
        'leao_pos': [1000, 250],
        'leao_speed': [-30,0],
        'contador_mortes': 0,
    }
    return window, assets, state