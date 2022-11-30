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