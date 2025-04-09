#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
n = random.randint(0,5) #fazendo o n aleatorio

tentativa = int(input('tente adivinhar o numero de 0 a 5: ')) #pedindo o numero

if tentativa == n:
    print("Você acertou parabens!")
else:
    print(f"voce nao acertou, o numero era {n}")









