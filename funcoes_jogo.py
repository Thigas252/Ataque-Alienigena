import sys
import pygame
from bala import Bala
from alien import Alien
from time import sleep

#Ouvir eventos do jogo

def ouvir_eventos(opc, tela, nave, balas):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                ouvir_keydown(event, opc, tela, nave, balas)
            elif event.type == pygame.KEYUP:
                ouvir_keyup(event, nave)

def ouvir_keydown(event, opc, tela, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.movendoDireita = True
    if event.key == pygame.K_LEFT:
        nave.movendoEsquerda = True
    if event.key == pygame.K_SPACE:
        nova_bala = Bala(opc, tela, nave)
        balas.add(nova_bala)   

def ouvir_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movendoDireita = False
    if event.key == pygame.K_LEFT:
        nave.movendoEsquerda = False

#Aliens

def aliens_horizontais(opc, alien_largura):
    espaco_disponivel_horizontal = opc.tela_largura
    numero_aliens_horizontal = int(espaco_disponivel_horizontal / (2 * alien_largura))
    return numero_aliens_horizontal

def aliens_vertical(opc, nave_altura, alien_altura):
    espaco_disponivel_vertical = opc.tela_altura - (3 * alien_altura) - nave_altura
    numero_aliens_vertical = int(espaco_disponivel_vertical / (2 * alien_altura))
    return numero_aliens_vertical

def criar_alien(opc, tela, aliens, numero_aliens_horizontal, numero_aliens_vertical):
    alien = Alien(tela, opc)
    alien_largura = alien.rect.width
    alien.x = alien_largura + 2 *  alien_largura * numero_aliens_horizontal
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_aliens_vertical
    aliens.add(alien)

def criar_frota(opc, tela, nave, aliens):
    alien = Alien(tela, opc)
    num_aliens_x = aliens_horizontais(opc, alien.rect.width)
    num_aliens_y = aliens_vertical(opc, nave.rect.height, alien.rect.height)
    for linha in range(num_aliens_y):
        for alien_horizontal in range(num_aliens_x):
            criar_alien(opc, tela, aliens, alien_horizontal, linha)

def verificar_lados_frota(opc, tela, nave, aliens, balas):
    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.verificar_posicao():
            mudar_dir_frota(opc, aliens)
            break

def verificar_fim_frota(opc, status, tela, nave, aliens, balas):
    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
            nave_reset(opc, status, tela, nave, aliens, balas)
            break

def mudar_dir_frota(opc, aliens):
    for alien in aliens.sprites():
        alien.rect.y += opc.alien_vel_b
    opc.alien_dir *= -1
    
#Atualizações de Posicão

def atualizar_balas(opc, tela, status, pontos, nave, aliens, balas):
    balas.update()

    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    print(len(balas))

    collision = pygame.sprite.groupcollide(balas, aliens, True, True)

    if collision:
        for alien in collision.values():
            status.pontos += opc.alien_pontos * len(aliens)
            pontos.prep_placar()

    if len(aliens) == 0:
        balas.empty()
        criar_frota(opc, tela, nave, aliens)

def atualizar_aliens(opc, status, tela, nave, aliens, balas):
    verificar_lados_frota(opc, tela, nave, aliens, balas)
    aliens.update()
    verificar_fim_frota(opc, status, tela, nave, aliens, balas)
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_reset(opc, status, tela, nave, aliens, balas)

#Nave

def nave_reset(opc,status, tela, nave, aliens, balas):
    if status.naves_restantes > 0:
        status.naves_restantes -= 1
        aliens.empty()
        balas.empty()
        nave.centralizar_nave()
        sleep(0.5)

def update_tela(opc, tela, status, pontuacao, nave, aliens, balas):
    tela.fill(opc.cor_fundo)
    nave.blitme()
    aliens.draw(tela)
    pontuacao.mostrar_placar()

    for bala in balas.sprites():
        bala.desenha_bala()
        
    pygame.display.flip()