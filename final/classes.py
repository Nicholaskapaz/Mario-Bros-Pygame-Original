import pygame
class pedra(pygame.sprite.Sprite):
    def _init_(self,groups,assets):
        pygame.sprite.Sprite_init_(self)

        self.image = assets['pedra']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.rect()
        self.rect.x = x
        self.rect.y = y