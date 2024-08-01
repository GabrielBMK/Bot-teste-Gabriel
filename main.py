from random import randint
from time import sleep

print('Estou pensando...')
sleep(2)
print('er...')
sleep(2)
computador = randint(1,10)
print('PRONTO TENTE ACERTAR!')
contador = 0
while True:
    contador += 1
    player = int(input('Chute um numero de 1 a 10: '))
    if computador == player:
        print(f'Parabéns!! você acertou com {contador} tentativa')
        print('Aposte ja na mega sena!!')
        break
    elif computador == player and contador > 2:
        print(f'Você acertou com {contador} tentativas, sua sorte está mediana')
    elif computador == player and contador > 5:
        print(f'Você está sem sorte, não aposte na mega sena!!')
    elif computador > player:
        print('Você chutou baixo!!')
    elif computador < player:
        print('Você chutou baixo!!')
    
