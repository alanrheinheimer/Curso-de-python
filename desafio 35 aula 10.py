#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.
r1 = float(input("Dgitite o comprimento da primeira reta: "))
r2 = float(input("digite o comprimento da segunda reta: "))
r3 = float(input("digite o comprimento da terceira reta"))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print("as retas podem formar um triangulo")
else:
    print("as retas nao podem formar um triangulo")