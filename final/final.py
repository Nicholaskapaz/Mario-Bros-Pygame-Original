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
    assets['mapa'] = pygame.image.load('sprites/fundo_pygame.png').convert_alpha()
    assets['mapa'] = pygame.transform.scale(assets['mapa'],(width,height))
    assets['personagem_maciel'] = pygame.image.load('sprites/personagem_maciel.png').convert_alpha()
    assets['personagem_maciel'] = pygame.transform.scale(assets['personagem_maciel'],(w_m,h_m))
    assets['maciel_pulando'] = pygame.image.load('sprites/maciel_pulando_png.png').convert_alpha()
    assets['maciel_pulando'] = pygame.transform.scale(assets['maciel_pulando'],(w_m,h_m))
    assets['pedra'] = pygame.image.load('sprites/pedra.png').convert_alpha()
    assets['pedra'] = pygame.transform.scale(assets['pedra'],(w_p,h_p))
    assets['leao'] = pygame.image.load('sprites/leao.png').convert_alpha()
    assets['leao'] = pygame.transform.scale(assets['leao'],(w_p+30,h_p+10))
    assets['caveira'] = pygame.image.load('sprites/caveira.png').convert_alpha()
    assets['caveira'] = pygame.transform.scale(assets['caveira'],(69,69))
    assets['coracao'] = pygame.image.load('sprites/heart.png').convert_alpha()
    assets['coracao'] = pygame.transform.scale(assets['coracao'],(69,69))
    assets['fonte_50'] = pygame.font.Font('final/ARCADE.ttf', 50)

 # Carrega os sons do jogo
    
    mixer.music.load('final/musica_pygame.mp3')
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

# Implementando mapa, pedra, leao, design da morte e vida, movimento

def desenha(window: pygame.Surface, assets, state):
    window.fill((0,0,0))
    window.blit(assets['mapa'], (0, 0))
    window.blit(assets['pedra'], (250, 250))
    window.blit(assets['leao'], (state['leao_pos'][0], state['leao_pos'][1]))

    for i in range(3):
        if i < state['contador_mortes']:
            window.blit(assets['caveira'], (i*69, 0))
        else:
            window.blit(assets['coracao'], (i*69, 0))

    if state['contador_mortes'] == 3:
            game_over_text = assets['fonte_50'].render('Morreu 3 vezes, o jogo acabou!', True, (255, 255, 255))
            window.blit(game_over_text, (250, 40))
            aperte_tecla_text = assets['fonte_50'].render('Aperte qualquer tecla para sair', True, (255, 255, 255))
            window.blit(aperte_tecla_text, (250, 200))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state['acabou'] = True
                        return False
                    elif event.type == pygame.KEYDOWN:
                        state['acabou'] = True
                        return False
                        
    if state['pulando']:
        window.blit(assets['maciel_pulando'], state['maciel_pos'])
    else:
        window.blit(assets['personagem_maciel'], state['maciel_pos'])
    pygame.display.update()

# Verifica se o personagem teve alguma colisao com a pedra ou leao

def personagem_bateu_na_pedra(state):
    if state['maciel_pos'][0] + 15 > 250 and state['maciel_pos'][0] < 250 + 35:
        if state['maciel_pos'][1] + 55 > 250 and state['maciel_pos'][1] < 250 + 40:
            return True
    return False

def personagem_bateu_no_leao(state):
    if state['maciel_pos'][0] + 15 > state['leao_pos'][0] and state['maciel_pos'][0] < state['leao_pos'][0] + 45:
        if state['maciel_pos'][1] + 50 > state['leao_pos'][1] and state['maciel_pos'][1] < state['leao_pos'][1] + 20:
            return True
    return False

# Atualiza o jogo, direciona a posiçao do personagem e objetos, faz as animaçoes do jogo

def atualiza_jogo(assets, state):
    if personagem_bateu_na_pedra(state) or personagem_bateu_no_leao(state):
        state['maciel_pos'] = [50,216]
        state['contador_mortes'] += 1
    time = pygame.time.get_ticks()
    tempo_por_atualizacao = (time - state['time_update']) / 1000
    state['maciel_pos'][0] += state['maciel_speed'][0] * tempo_por_atualizacao
    state['maciel_speed'][1] += state['gravidade'] * tempo_por_atualizacao
    state['maciel_pos'][1] += state['maciel_speed'][1] * tempo_por_atualizacao
    state['leao_pos'][0] += state['leao_speed'][0] * tempo_por_atualizacao

    if state['maciel_pos'][1] > 216:
        state['maciel_pos'][1] = 216
        state['pulando'] = False

    if state['leao_pos'][0] < 50:
        state['leao_speed'][0] *= -1
        state['leao_pos'][0] = 50
        assets['leao'] = pygame.transform.flip(assets['leao'], True, False)
    if state['leao_pos'][0] > 1150:
        state['leao_speed'][0] *= -1
        state['leao_pos'][0] = 1150
        assets['leao'] = pygame.transform.flip(assets['leao'], True, False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['acabou'] = True
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state['maciel_speed'][0] = -100
            if event.key == pygame.K_RIGHT:
                state['maciel_speed'][0] = 100
            if event.key == pygame.K_SPACE and not state['pulando']:
                state['maciel_speed'][1] = -100
                state['pulando'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                state['maciel_speed'][0] = 0
    state['time_update'] = time

# Funçao do Loop do jogo
def loop_jogo(window, assets, state):
    while state['acabou'] == False:
        desenha(window, assets, state)
        atualiza_jogo(assets, state)

# Finalizaçao do jogo 
def finaliza_jogo():
    pygame.quit()

if _name_ == "_main_":
    window, assets, state = inicializa_jogo()
    loop_jogo(window, assets, state)
    finaliza_jogo()
