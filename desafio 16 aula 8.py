#Exercício Python 016: Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.
''''import math
numero = float(input("digite um numero real: "))
inteira = math.trunc(numero)
print(f"o {numero} tem a parte inteira {inteira}")'''''

''''from math import trunc
numero = float(input("digite um numero: "))
print(f"você digitou o numero {numero} que tem a parte inteira {trunc(numero)}")'''''

num = float(input("digite um numero"))
print(f"o valor digitado foi {num}  e sua parte inteira é: {int(num)}")
