# Gerador de registro

#   obter nome e idade
#   registrar automaticamente a data de cadastro do usuario
#   cada usuario registrado recebe um cartao abaixo de forma aleatoria
#   cartões = [50, 250, 120]
#
# mensagem de boas vindas

from datetime import datetime
from random import choice

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
data_registro = datetime.now()

cartoes = ['R$50,00', 'R$120,00', 'R$250,00']
sorteio = choice(cartoes)

print(f'Olá {nome}! Seu registro foi concluído com sucesso'
      f'no dia {data_registro.day}/{data_registro.month}/{data_registro.year}\n'
      f'Parabéns! Houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}')
