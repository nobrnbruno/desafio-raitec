import pygame as pg
import random
import PySimpleGUI as sg

# cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (15, 157, 8)
marrom = (80, 48, 30)

# tela do jogo
largura, altura = 800, 600
window = pg.display.set_mode((largura, altura))
pg.display.set_caption("Jogo da forca")

# fonte do jogo
pg.font.init()
font_giz_peq = pg.font.Font('chawp.ttf', 30)
font_giz_grd = pg.font.Font('Chalk-Regular.ttf', 50)

# palavras possiveis
# listas de palavras (o nome da lista é o tipo)
objeto = ["caneta", "relogio", "tesoura", "abajur", "chaveiro"]
comida = ["pizza", "salada", "sanduiche", "pudim", "macarrao"]
fruta = ["maca", "banana", "uva", "laranja", "abacaxi"]
lugar = ["praia", "parque", "cinema", "livraria", "shopping"]
transporte = ["bicicleta", "carro", "onibus", "aviao", "trem"]

lista_tipo = [objeto, comida, fruta, lugar,
              transporte]  # lista das listas de tipo

# iniciando as variaveis
tipo_palavra = [' ', '-']
tentativas = []
nomes = []
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chances = 0
letra = ''


def desenho_da_forca(window, chances):
    background_image = pg.image.load("lousa.jpg").convert()  # escolhe a imagem
    background_image = pg.transform.scale(
        background_image, (largura, altura))  # redimensiona a imagem
    window.blit(background_image, (0, 0))

    pg.draw.line(window, marrom, (80, 500), (80, 100), 10)
    pg.draw.line(window, marrom, (30, 500), (130, 500), 10)
    pg.draw.line(window, marrom, (76, 100), (245, 100), 10)
    pg.draw.line(window, marrom, (240, 100), (240, 150), 10)

    if chances >= 1:
        pg.draw.circle(window, branco, (240, 200), 50, 10)
    if chances >= 2:
        pg.draw.line(window, branco, (240, 250), (240, 350), 10)
    if chances >= 3:
        pg.draw.line(window, branco, (240, 260), (175, 350), 10)
    if chances >= 4:
        pg.draw.line(window, branco, (240, 260), (305, 350), 10)
    if chances >= 5:
        pg.draw.line(window, branco, (240, 350), (305, 450), 10)
    if chances >= 6:
        pg.draw.line(window, branco, (240, 350), (175, 450), 10)


def Nome_tipo(lista):
    # função que retorna a lista da categoria escolhida e seu nome
    tipo_palavra = random.choice(lista)  # escolhe aleatoriamente uma categoria
    for nome, valor in globals().items():
        if valor == tipo_palavra:
            return nome.upper(), tipo_palavra
    return None


def Sorteando_palavra_e_tipo(lista_tipo, tipo_palavra, palavra_escolhida, nomes, end_game):
    if end_game == True:
        # sorteando o tipo e salvando seu nome
        nome, tipo_palavra = Nome_tipo(lista_tipo)
        # armazena o nome nessa lista, para ser usado para aparecer na tela
        nomes.append(nome)
        palavra_escolhida = random.choice(tipo_palavra)
        end_game = False
    return palavra_escolhida, nomes, end_game


def Camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas):
    palavra_camuflada = ''
    for letra in palavra_escolhida:
        if letra in tentativas:
            palavra_camuflada += letra + '  '
        else:
            palavra_camuflada += '_ '
    return palavra_camuflada.strip()


def Tentativa_de_letra(tentativas, palavra_escolhida, letra, chances):
    if letra not in tentativas:
        tentativas.append(letra)
        if letra not in palavra_escolhida:
            chances += 1
            if chances > 6:
                chances = 6  # apenas garantindo que ele só tem essas 6 chances
    elif letra in tentativas:
        pass
    return chances, tentativas


def Palavra_do_jogo(palavra_escolhida, window):
    palavra = font_giz_peq.render(palavra_camuflada.upper(), True, branco)
    window.blit(palavra, (360, 475))


def Ganhou(palavra_escolhida, tentativas):  # função para checar se ganhou o jogo
    ganhou = True

    for n in palavra_escolhida:
        if n not in tentativas:
            ganhou = False

    if ganhou == True:
        return True
    else:
        return False


def Popup_Escolha(ganhou):
    # função para criar o popup pra decidir se continua jogando ou não

    layout_ganhar = [  # Layout dos botões caso ganhar
        [sg.Text('Parabéns, você venceu, a palavra era:'),
         sg.Text(palavra_escolhida.upper())],
        [sg.Text('Deseja tentar novamente?')],
        [sg.B('Sim !', button_color='Green'),
         sg.B('Não.', button_color='Red')],
    ]

    layout_perder = [  # Layout do botões caso perder
        [sg.Text("Que pena, você perdeu, a palavra era:"),
         sg.Text(palavra_escolhida.upper())],
        [sg.Text("Deseja tentar novamente?")],
        [sg.B('Sim !', button_color='Green'),
         sg.B('Não.', button_color='Red')],
    ]

    # Verifica se ganhou e cria o popup baseado nisso
    if ganhou == True:
        Window = sg.Window('Fim de jogo', layout_ganhar)

    else:
        Window = sg.Window('Fim de jogo', layout_perder)

    events, values = Window.read()  # lê o valor no qual o botão clicado fornece

    if events == 'Sim !':  # Se ele disse sim, sorteia a palavra novamente e fecha o popup
        end_game = True
        Sorteando_palavra_e_tipo(
            lista_tipo, tipo_palavra, palavra_escolhida, nomes, end_game)
        Window.close()

    else:
        end_game = True  # Se ele disse não, fecha tudo
        Window.close()
        pg.quit()
        quit()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).lower()

    # jogo

    desenho_da_forca(window, chances)
    palavra_escolhida, nomes, end_game = Sorteando_palavra_e_tipo(
        lista_tipo, tipo_palavra, palavra_escolhida, nomes, end_game)
    palavra_camuflada = Camuflando_palavra(
        palavra_escolhida, palavra_camuflada, tentativas)
    chances, tentativas = Tentativa_de_letra(
        tentativas, palavra_escolhida, letra, chances)
    Palavra_do_jogo(palavra_escolhida, window)

    # mostrando a categoria na tela
    # pega a ultima posição da lista nomes e mostra na tela
    texto = font_giz_grd.render(nomes[len(nomes) - 1], True, branco)
    window.blit(texto, (435, 150))

    texto_principal = font_giz_grd.render('Jogo  da  Forca', True, branco)
    window.blit(texto_principal, (220, 20))

    # reiniciando o jogo
    if (chances >= 6 or Ganhou(palavra_escolhida, tentativas) == True):

        end_game = True

        if (Ganhou(palavra_escolhida, tentativas) == True):
            ganhou = True  # Diz que ele ganhou para aparecer o popup correto
            Popup_Escolha(ganhou)

            # Reinicia todas as variáveis
            tentativas = [' ', '-']
            chances = 0
            letra = ''
            tipo_palavra = []

        else:
            ganhou = False  # Diz que ele não ganhou para aparecer o popup correto
            Popup_Escolha(ganhou)

            # Reinicia todas as variáveis
            tentativas = [' ', '-']
            chances = 0
            letra = ''
            tipo_palavra = []

    pg.display.update()
