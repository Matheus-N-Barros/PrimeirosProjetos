# exercicio 9 - tabuada

print('*' * 30)
num = input('Digite o número da tabuada ')

try:
    num = int(num)
except ValueError:
    i = 0
    while ValueError:
        num = input('Inválido. Digite um número inteiro ')
        try:
            num = int(num)
            break
        except ValueError:
            i += 1

print(f'Tabuada do {num}')
print('*' * 30)

for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')
