import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self, opc, tela, nave):
        super().__init__()

        self.tela = tela

        self.rect = pygame.Rect(0,0, opc.bala_largura, opc.bala_altura)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        self.y = float(self.rect.y)

        self.cor = opc.bala_cor
        self.velocidade = opc.bala_vel

    def update(self):
        self.y -= self.velocidade
        self.rect.y = self.y

    def desenha_bala(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)