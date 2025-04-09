#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na
# tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input("digite algo: ")
print("aqui estao informações sobre o numero")
print("tipo primitivo: ",type(n))
print("alphanumerico: ",n.isalnum())
print("numerico: ",n.isnumeric())
print("alpha: ", n.isalpha())

