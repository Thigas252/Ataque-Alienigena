import sys
import pygame

from config import Opcoes
from nave import Nave
from bala import Bala
from alien import Alien
from status import StatusJogo
from placar import Placar

import funcoes_jogo as FJ
from pygame.sprite import Group


def rodar_jogo():
    pygame.init()

    #Instancias
    opc = Opcoes()
    status = StatusJogo(opc)
    
    tela = pygame.display.set_mode((opc.tela_largura, opc.tela_altura))
    status.resetStatus()
    pontuacao = Placar(opc,tela,status)
    pygame.display.set_caption("Invasão Alienigena")

    balas = Group()
    aliens = Group()

    nave = Nave(tela, opc)
    FJ.criar_frota(opc, tela, nave, aliens)

    while True:
        FJ.ouvir_eventos(opc, tela, nave, balas)
        FJ.update_tela(opc, tela, status, pontuacao, nave, aliens, balas)
        FJ.atualizar_balas(opc, tela, status, pontuacao, nave, aliens, balas)
        FJ.atualizar_aliens(opc, status,  tela, nave, aliens, balas)
        nave.update()
        
        
rodar_jogo()

