import pygame as pg
import random

# cores #
verde = (29, 89, 35)
branco = (220, 220, 220)

# tela #
janela = pg.display.set_mode((900, 600))

# fonte: inicialização e declaração #
pg.font.init
fonteGiz = pg.font.Font('Chalk-Regular.ttf', 50)
fonteSistema = pg.font.SysFont('Courier New', 30)

# variáveis gerais de jogo #
palavras = ['BURACO', 'ANALISE', 'TOSQUEAR', 'XICARA DE CAFE']
palavraEscolhida = ''
palavraAnonima = ''
tentativasDeLetras = [' ', '-', '–', '-', '_', '—']
chances = 0
letra = ''
terminarJogo = True
statusClique = False

# loop de execução do jogo #
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit
