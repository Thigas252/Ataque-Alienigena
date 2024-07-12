import pygame

class Nave():
    def __init__(self, tela, opc):
      self.tela = tela
      self.opc = opc
      self.tela_rect = tela.get_rect()

      self.imagem = pygame.image.load("nave.png")
      self.rect = self.imagem.get_rect()

      self.rect.centerx = self.tela_rect.centerx
      self.rect.bottom = self.tela_rect.bottom

      self.movendoDireita = False
      self.movendoEsquerda = False

    def blitme(self):
        self.tela.blit(self.imagem, self.rect)

    def centralizar_nave(self):
       self.center = self.tela_rect.centerx

    def update(self):
        if self.movendoDireita and self.rect.right < self.tela_rect.right:
          self.rect.centerx += 1
        if self.movendoEsquerda and self.rect.left > 0:
           self.rect.centerx -= 1
