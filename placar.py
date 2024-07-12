import pygame.font
from pygame.sprite import Group
from nave import Nave

class Placar():
    def __init__(self, opc, tela, status):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.opc = opc
        self.status = status

        self.texto_cor = (30,30,30)
        self.fonte = pygame.font.SysFont(None,48)

        self.prep_placar()
    
    def prep_placar(self):
        placar_str = str(self.status.pontos)
        self.placar_imagem = self.fonte.render(placar_str, True, self.texto_cor, self.opc.cor_fundo)

        self.placar_rect = self.placar_imagem.get_rect()
        self.placar_rect.right = self.tela_rect.right - 20
        self.placar_rect.top = 20
    
    def mostrar_placar(self):
        self.tela.blit(self.placar_imagem, self.placar_rect)
    
    def resetStatus(self):
        self.naves_restantes = self.opc.nave_vidas
        self.pontos = 0