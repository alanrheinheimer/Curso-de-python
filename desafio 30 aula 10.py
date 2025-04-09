#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("digite um numero inteiro qualquer: "))

if n %2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")