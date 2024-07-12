import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, tela, opc):
        super().__init__()
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.opc = opc

        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.opc.alien_vel * self.opc.alien_dir)

        self.rect.x = self.x

    def verificar_posicao(self):
        if self.rect.right >= self.tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.tela.blit(self.image, self.rect)