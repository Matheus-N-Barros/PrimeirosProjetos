# Mini Game - Desenho com módulo Turtle

from turtle import Turtle  # importa a funcao Turtle do módulo turtle
tortuguita = Turtle()  # cria a turtle
tortuguita.shape("turtle")  # escolhe a forma da turtle
tortuguita.speed(1)  # escolhe a velocidade da turtle

continua = True  # o programa continua rodando até o usuário decidir parar
while continua:
    direcao = input('Digite a direção da tartaruga "Frente: F ou Trás: T": ')
    distancia = float(input('Digite a distância a ser percorrida: '))

    if direcao == 'F' or direcao == 'f':
        tortuguita.forward(distancia)
    elif direcao == 'T' or direcao == 't':
        tortuguita.backward(distancia)

    rotacao = input('Deseja rotacionar a tartaruga? S ou N: ')
    if rotacao == 's' or rotacao == 'S':

        quero_rotacao = input('Rotacionar p/ a direita ou p/ a esquerda? D ou E: ')
        if quero_rotacao == 'd' or quero_rotacao == 'D':
            graus = float(input('Digite em quantos graus rotacionar: '))
            tortuguita.right(graus)
        elif quero_rotacao == 'e' or quero_rotacao == 'E':
            graus = float(input('Digite em quantos graus rotacionar: '))
            tortuguita.left(graus)

    elif rotacao == 'n' or rotacao == 'N':
        resposta = input('Deseja continuar andando? S ou N: ')
        if resposta == 'n' or resposta == 'N':
            input()
            continua = False
