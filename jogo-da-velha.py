#Jogo da velha

import os
import random
from colorama import Fore

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1 = CPU | #2 = Jogador
maxJogadas = 9
vencedor = ""
tabuleiro = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]
             ]


def mostrar_tabuleiro():
    global tabuleiro
    global jogadas
    os.system("cls")
    print("     1    2    3")
    print("1:    " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("    -------------")
    print("2:    " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("    -------------")
    print("3:    " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..: "))
            l = l - 1

            c = int(input("Coluna.: "))
            c = c - 1
        except:
            print("Digite um valor valido!")

        try:
            while tabuleiro[l][c] != "-":
                l = int(input("Linha..: "))
                l = l - 1

                c = int(input("Coluna.: "))
                c = c - 1

            tabuleiro[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Espaço inválido!")


def cpuJoga():
    global jogadas
    global maxJogadas
    global quemJoga

    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while tabuleiro[l][c] != "-":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)

        tabuleiro[l][c] = "O"
        quemJoga = 2
        jogadas += 1


def verificarVitoria():
    global tabuleiro
    vitoria = "n"
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "n"
        il = ic = 0

        # verifica linhas
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if tabuleiro[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1

        if vitoria != "n":
            break

        # verifica colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if tabuleiro[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1

        if vitoria != "n":
            break

        # verifica diagonal e-d
        soma = 0
        idiag = 0

        while idiag < 3:
            if tabuleiro[idiag][idiag] == s:
                soma += 1
            idiag += 1
        if soma == 3:
            vitoria = s
            break

        # verifica diagonal d-e
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if tabuleiro[idiagl][idiagc] == s:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria
    # verifica diagonal d-e


def redefinir():
    global tabuleiro
    global jogadas
    global quemJoga
    global maxJogadas
    global vencedor
    jogadas = 0
    quemJoga = 2  # 1 = CPU | #2 = Jogador
    maxJogadas = 9
    vencedor = ""
    tabuleiro = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


while jogarNovamente == "s":
    while True:
        mostrar_tabuleiro()
        jogadorJoga()
        cpuJoga()
        vencedor = verificarVitoria()
        if (vencedor != "n") or (jogadas >= maxJogadas):
            break

    print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
    if vencedor == "X":
        mostrar_tabuleiro()
        print(Fore.BLUE + "Resultado: Você venceu!" + Fore.RESET)
    elif vencedor == "O":
        mostrar_tabuleiro()
        print(Fore.RED + "A CPU venceu" + Fore.RESET)
    else:
        print("Resultado: Empate")
    jogarNovamente = input(Fore.BLUE + "Digite [s] para continuar ou [n] para sair: " + Fore.RESET)
    redefinir()