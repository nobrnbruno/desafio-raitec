palavra = "PYTHON"
letras_input = []
chances = 10
ganhou = False

while True:
    for letra in palavra:
        if letra.upper() in letras_input:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")

    tentativa = input("Escolha uma letra para adivinhar: ")
    print("")
    letras_input.append(tentativa.upper())

    ganhou = True

    for letra in palavra:
        if letra.upper() not in letras_input:
            ganhou = False

    if tentativa.upper() not in palavra.upper():
        chances -= 1

    if chances == 0 or ganhou:
        break

if ganhou:
    print(letras_input)
    print("Parabéns, você ganhou!")
else:
    print(f"Voce perdeu. A palavra era: {palavra}")
