#Escreva um Programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.O progrma deverá escrever na tela se o usuário venceu ou perdeu
#codigo ansi para colocar cor ex:/033[0:ex:style,33ex:text,44back m

from time import sleep
from random import randint
computador = randint(0,100) #faz o computador fazer "pensar"
print("=="*20)
print('vou pensar em um número entre 0 e 5. Tente advinhar...')
print("=="*20)
jogador= int(input('em que número eu pensei? '))#Jogador tentar advinhar

print('\033[36mPROCESSANDO... \033]m ')
sleep(2)#para dar tempo antes do programa responder
if jogador == computador:
    print('Vc ganhou!!')
else:
    print('vc perdeu. eu pensei no número {}'.format(computador))
