#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#  80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
#  Km acima do limite.

v = float(input("qual a velocidade do carro?")) #velocidade do carro

multa = (v-80)*7

if v > 80:
    print(f"voce foi multado em {multa} reais.")