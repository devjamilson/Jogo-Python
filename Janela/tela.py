import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1366
altura = 710

x = largura/2
y = altura/2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Joguinho sem nome ainda')

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        

        '''controlando um objeto'''
        if pygame.key.get_pressed()[K_1]:
            x = x - 20
        if pygame.key.get_pressed()[K_3]:
            x = x + 20
         


    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    pygame.display.update()
