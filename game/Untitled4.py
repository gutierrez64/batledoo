#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

pygame.mixer.music.set_volume(0.1)

musica_de_fundo = pygame.mixer.music.load('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/batledoo/songs/BoxCat Games - Inspiration.mp3')
pygame.mixer.music.play(-1)

barulho_tiro_acerto = pygame.mixer.Sound('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/batledoo/songs/smw_yoshi_stomp.wav')
barulho_tiro_erro = pygame.mixer.Sound('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/batledoo/songs/smw_yellow_yoshi_stomp.wav')
barulho_zerolife = pygame.mixer.Sound('C:/Users/Matheus/OneDrive/Documentos/Projetos/python/pygame/batledoo/songs/smw_bowser_fire.wav')


barulho_tiro_acerto.set_volume(0.5)
barulho_tiro_erro.set_volume(0.5)

largura = 640
altura = 480

x_player = largura/2
y_player = altura/2


x_bala = largura/2
y_bala = altura/2

x_mob = 0
y_mob = 120

x_mob2 = 640
y_mob2 = 100

points = 0
life = 10

fonte_texto = pygame.font.SysFont('arial', 40, True, False)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura,altura))


while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    texto = f'Points: {points}    Lifes: {life}'
    texto_formatado = fonte_texto.render(texto, False, (255,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bala = pygame.draw.circle(tela, (255,255,0), (x_bala,130), 2)
                if bala.colliderect(mob):
                    barulho_tiro_acerto.play()
                    x_mob = -40
                    points = points + 1
                else:
                    barulho_tiro_erro.play()
                
                    
                    
                if bala.colliderect(mob2):
                            life = life + 10
                
    
    #animação
    if x_mob <= 1000:
        x_mob += 5
    
    if x_mob >= 640:
        x_mob = -40
        life = life - 1
        #reset
        if life == 0:
            barulho_zerolife.play()
            points = 0
            life = 10
    
    
    if points > 10:
        x_mob += 5
        mob2 = pygame.draw.rect(tela, (255, 255, 255), (x_mob2, y_mob2, 50, 50))
        if x_mob2 <= 1000:
            x_mob2 -= 5
        
        
    player = pygame.draw.rect(tela, (255, 0, 0), (x_player, 400, 40, 40))
    mob = pygame.draw.rect(tela, (0, 0, 255), (x_mob, y_mob, 40, 40))
    
    (x_player,y_player) = pygame.mouse.get_pos()
    (x_bala,y_bala) = pygame.mouse.get_pos()
    
    tela.blit(texto_formatado, (50,40))
    pygame.display.update()


# In[ ]:





# In[ ]:




