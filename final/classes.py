import pygame

# Implementando as classes, da pedra, personagem_maciel

class pedra(pygame.sprite.Sprite):
    def _init_(self,groups,assets):
        pygame.sprite.Sprite_init_(self)

        self.image = assets['pedra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.rect()
        self.rect.x = x
        self.rect.y = y

class Personagem_Maciel(pygame.sprite.Sprite):


    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['personagem_maciel']
        self.maciel_padrao = True
        self.maciel_pular = False
        self.step_index = 0 
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.groups = groups
        self.assets = assets
        self.speedx = 0
        self.speedy = 0 