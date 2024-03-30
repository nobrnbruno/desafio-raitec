import pygame as pg
import random

# cores #
verde = (29, 89, 35)
branco = (220, 220, 220)
preto = (10, 10, 10)

# tela #
janela = pg.display.set_mode((900, 600))

# fonte: inicialização e declaração #
pg.font.init()
fonteGiz = pg.font.Font('chawp.ttf', 50)
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


def DesenharForca(janela, chances):
    # essa função desenha background, forca e pessoa na forca #
    pg.draw.rect(janela, verde, (0, 0, 900, 600))
    pg.draw.line(janela, branco, (100, 500), (100, 100), 10)
    pg.draw.line(janela, branco, (50, 500), (150, 500), 10)
    pg.draw.line(janela, branco, (96, 100), (305, 100), 10)
    pg.draw.line(janela, branco, (300, 100), (300, 150), 10)
    if chances >= 1:
        # cabeça
        pg.draw.circle(janela, branco, (300, 200), 50, 10)
    if chances >= 2:
        # tronco
        pg.draw.line(janela, branco, (300, 250), (300, 350), 10)
    if chances >= 3:
        # braço direito
        pg.draw.line(janela, branco, (300, 260), (225, 350), 10)
    if chances >= 4:
        # braço esquerdo
        pg.draw.line(janela, branco, (300, 260), (375, 350), 10)
    if chances >= 5:
        # perna direita
        pg.draw.line(janela, branco, (300, 350), (375, 450), 10)
    if chances >= 6:
        # perna direita
        pg.draw.line(janela, branco, (300, 350), (225, 450), 10)


def Desenhar_Botao_Restart(janela):
    # botão restart #
    pg.draw.rect(janela, preto, (600, 100, 200, 65))
    texto = fonteSistema.render('Recomeçar', 1, branco)
    janela.blit(texto, (620, 120))


def Sortear_Palavra(palavras, palavraEscolhida, terminarJogo):
    if terminarJogo == True:
        palavraIndice = random.randint(0, len(palavras) - 1)
        palavraEscolhida = palavras[palavraIndice]
        terminarJogo = False
        chances = 0
    return palavraEscolhida, terminarJogo


def Camuflar_Palavra(palavraEscolhida, palavraAnonima, tentativasDeLetras):
    palavraAnonima = palavraEscolhida
    for n in range(len(palavraAnonima)):
        if palavraAnonima[n:n + 1] not in tentativasDeLetras:
            palavraAnonima = palavraAnonima.replace(
                palavraAnonima[n], '_')
    return palavraAnonima


def Escrever_Palavra(window, palavraAnonima):
    palavra = fonteSistema.render(palavraAnonima, 1, branco)
    window.blit(palavra, (200, 500))


def Tentar_Letra(tentativasDeLetras, palavraEscolhida, letra, chances):
    if letra not in tentativasDeLetras:
        tentativasDeLetras.append(letra)
        if letra not in palavraEscolhida:
            chances += 1
    elif letra in tentativasDeLetras:
        pass
    return tentativasDeLetras, chances


def Recomecar_Jogo(palavraAnonima, terminarJogo, chances, letra, tentativasDeLetras, statusClique, click, x, y):
    count = 0
    limite = len(palavraAnonima)
    for n in range(len(palavraAnonima)):
        if palavraAnonima[n] != '#':
            count += 1
    if count == limite and statusClique == False and click[0] == True:
        print('Ok')
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativasDeLetras = [' ', '-', '–', '-', '_', '—']
            terminarJogo = True
            chances = 0
            letra = ' '
    return terminarJogo, chances, tentativasDeLetras, letra


# loop de execução do jogo #
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit
        if evento.type == pg.KEYDOWN:
            letra = str(pg.key.name(evento.key)).upper()
            print(letra)

    # variáveis da posição do mouse #
    mouse = pg.mouse.get_pos()
    mousePosicaoX = mouse[0]
    mousePosicaoY = mouse[1]

    # variavel do click do mouse #
    click = pg.mouse.get_pressed()

    # rodando o jogo #
    DesenharForca(janela, chances)
    Desenhar_Botao_Restart(janela)
    palavraEscolhida, terminarJogo = Sortear_Palavra(
        palavras, palavraEscolhida, terminarJogo)
    palavraAnonima = Camuflar_Palavra(
        palavraEscolhida, palavraAnonima, tentativasDeLetras)
    tentativasDeLetras, chances = Tentar_Letra(
        tentativasDeLetras, palavraEscolhida, letra, chances)
    Escrever_Palavra(janela, palavraAnonima)
    terminarJogo, chances, tentativasDeLetras, letra = Recomecar_Jogo(
        palavraAnonima, terminarJogo, chances, letra, tentativasDeLetras, statusClique, click, mousePosicaoX, mousePosicaoY)
    print(palavraEscolhida, palavraAnonima)

    # Click Last Status
    if click[0] == True:
        statusClique = True
    else:
        statusClique = False

    pg.display.update()
