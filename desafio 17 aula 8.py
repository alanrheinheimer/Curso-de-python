#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento
# da hipotenusa.

'''cata = float(input("digite o cateto adjacente: "))
cato = float(input("digite o cateto oposto: "))
hip = (cata**2+cato**2)**0.5
print(f"o valor da hipotenusa é: {hip}")'''

''''import math
cata = float(input(("digite o cateto adjacente: ")))
cato = float(input("digite o cateto oposto:"))
print(f"o valor da hipotenusa é:{math.sqrt(cata**2+cato**2):.2f} ")'''

import math
cata = float(input("digite o cateto adjacente: "))
cato = float(input("digite o cateto oposto: "))
print(f"o valor da hipotenusa é: {math.hypot(cata,cato):.2f}")






