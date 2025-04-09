#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
from itertools import count

nome = str(input("nome completo: ")).strip()
print(f"seu nome em letras maiusculas é: {nome.upper()}")
print(f"seu nome em letras minusculas é: {nome.lower()}")

print(f"seu nome tem ao todo {len(nome)-nome.count(" ")} letras")

#print(f"seu primeiro nome tem {nome.find(" ")} letras") ---- soluçao pode aparecer erro se usuaria digitar só um nome.

primeironome = nome.split()[0]

print(f"seu primeiro nome tem {len(primeironome)} letras.")




