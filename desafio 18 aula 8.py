#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
ang = float(input("digite o angulo que você deseja: "))
angr = math.radians(ang)
print(f"o angulo de {ang} tem o seno de {math.sin(angr):.2f}")
print(f"o angulo de {ang} tem o cosseno de {math.cos(angr):.2f}")
print(f"o angulo de {ang} tem a tangente de {math.tan(angr):.2f}")