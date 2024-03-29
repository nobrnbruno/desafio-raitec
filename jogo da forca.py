import pygame as pg
import random
import PySimpleGUI as sg

#cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (15, 157, 8)
marrom = (80, 48, 30)

#tela do jogo
largura, altura = 800, 600
window = pg.display.set_mode((largura, altura))
pg.display.set_caption("Imagem de Fundo")

#fonte do jogo
pg.font.init()

font = pg.font.SysFont('Courier new', 35)
font_textop = pg.font.SysFont('Courier new', 50)

#palavras possiveis

fruta = ["banana", "laranja", "maracuja", "limao"] # listas de palavras (o nome da lista é o tipo)
objeto = ["borracha", "caneta", "lapis"]
automovel = ["carro", "moto", "caminhao"]

lista_tipo = [fruta, objeto, automovel] #lista das listas de tipo

#iniciando as variaveis
tipo_palavra = [' ', '-']
tentativas = []
nomes = []
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chances = 0
letra = ''


def desenho_da_forca(window, chances):
    background_image = pg.image.load("lousa.jpg").convert() #escolhe a imagem
    background_image = pg.transform.scale(background_image, (largura, altura)) #redimensiona a imagem
    window.blit(background_image, (0, 0))

    pg.draw.line(window, marrom, (100, 500), (100, 100), 10)
    pg.draw.line(window, marrom, (50, 500), (150, 500), 10)
    pg.draw.line(window, marrom, (100, 100), (300, 100), 10)
    pg.draw.line(window, marrom, (300, 100), (300, 150), 10)

    if chances >= 1:
        pg.draw.circle(window, branco, (300, 200), 50, 10)
    if chances >= 2:
        pg.draw.line(window, branco, (300, 250), (300, 350), 10)
    if chances >= 3:
        pg.draw.line(window, branco, (300, 260), (225, 350), 10)
    if chances >= 4:
        pg.draw.line(window, branco, (300, 260), (375, 350), 10)
    if chances >= 5:
        pg.draw.line(window, branco, (300, 350), (375, 450), 10)
    if chances >= 6:
        pg.draw.line(window, branco, (300, 350), (225, 450), 10)


#função que retorna a lista da categoria escolhida e seu nome
def Nome_tipo(lista):
    tipo_palavra = random.choice(lista) #escolhe aleatoriamente uma categoria
    for nome, valor in globals().items():
        if valor == tipo_palavra:
            return nome.upper(), tipo_palavra
    return None

def Sorteando_palavra_e_tipo(lista_tipo, tipo_palavra, palavra_escolhida, nomes, end_game):
    if end_game == True:
     nome, tipo_palavra = Nome_tipo(lista_tipo) #sorteando o tipo e salvando seu nome
     nomes.append(nome) #armazena o nome nessa lista, para ser usado para aparecer na tela
     palavra_escolhida = random.choice(tipo_palavra)
     end_game = False
    return palavra_escolhida, nomes, end_game

def Camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas:
          palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '_')
    return palavra_camuflada

def Tentativa_de_letra(tentativas, palavra_escolhida, letra, chances):
    if letra not in tentativas:
        tentativas.append(letra)
        if letra not in palavra_escolhida:
            chances += 1
            if chances > 6:
                chances = 6 # apenas garantindo que ele só tem essas 6 chances
    elif letra in tentativas:
     pass
    return chances, tentativas

def Palavra_do_jogo(palavra_escolhida, window):
    palavra = font.render(palavra_camuflada, True, branco)
    window.blit(palavra, (450, 450))

def Ganhou(palavra_escolhida, tentativas):  # função para checar se ganhou o jogo
    ganhou = True

    for n in palavra_escolhida:
        if n not in tentativas:
            ganhou = False

    if ganhou == True:
        return True
    else:
        return False

def Popup_Escolha(ganhou): # função para criar o popup pra decidir se continua jogando ou não

    layout_ganhar = [ # Layout dos botões caso ganhar
            [sg.Text('Parabéns, você venceu. Deseja jogar novamente ?')],
            [sg.B('Sim !', button_color='Green'), sg.B('Não.', button_color='Red')],
            ]
    
    layout_perder = [ # Layout do botões caso perder
            [sg.Text("Que pena, você perdeu. Deseja jogar novamente ?")],
            [sg.B('Sim !', button_color='Green'), sg.B('Não.', button_color='Red')],
            ]

    # Verifica se ganhou e cria a tela baseado nisso
    if ganhou == True: 
        window = sg.Window('Fim de jogo', layout_ganhar) 

    else:
        window = sg.Window('Fim de jogo', layout_perder)

    events, values = window.read() # lê o valor no qual o botão clicado fornece

    # Se o botão clicado for o de sim, vai retornar verdadeiro, reiniciando, ou falso, saindo
    if events == 'Sim !': # ainda preciso mexer nisso (1)
        end_game = False
    else:
        end_game = True
    


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).lower()

    
    #reiniciando o jogo
    if(chances == 6 or Ganhou(palavra_escolhida, tentativas) == True):
       
        end_game = True
        tentativas = [' ', '-']
        chances = 0
        letra = ''
        tipo_palavra = []
        
    #jogo
        
    desenho_da_forca(window, chances)
    palavra_escolhida, nomes, end_game = Sorteando_palavra_e_tipo(lista_tipo, tipo_palavra, palavra_escolhida, nomes, end_game)
    palavra_camuflada = Camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas)
    chances, tentativas = Tentativa_de_letra(tentativas, palavra_escolhida, letra, chances)
    Palavra_do_jogo(palavra_escolhida, window)


    #mostrando a categoria na tela
    texto = font.render(nomes[len(nomes) - 1], True, branco) #pega a ultima posição da lista nomes e mostra na tela
    window.blit(texto, (450, 100))

    texto_principal = font_textop.render('Jogo Da Forca', True, branco)
    window.blit(texto_principal, (220, 20))   

    
    pg.display.update()