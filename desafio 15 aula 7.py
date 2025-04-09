# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule
# o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmp = float(input("quantos km percorreu?: "))
dias = int(input("quantos dias ficou com o carro?:"))

debito = kmp * 0.15 + dias*60

print(f"valor a pagar é de: {debito:.2f}")