#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta
# viagens mais longas.d = float(input("qual a distancia da viagem? "))

if d <= 200:
    print(f"o valor da viagem é {d*0.50} reais")
else :
    print(f"o valor da viagem é: {d*0.45}")

