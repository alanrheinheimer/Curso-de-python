#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("digite o ano: "))
if ano % 4 == 0:
    print("o ano é bisexto")
else:
    print("o ano não é bisexto")