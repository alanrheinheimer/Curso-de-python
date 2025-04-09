#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "SILVA" no nome.
n = str(input("qual o seu nome completo? ")).strip()
print(f"seu nome tem Silva? {'silva' in n.lower()}")