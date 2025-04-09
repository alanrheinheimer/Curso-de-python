#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
preco = float(input("preço do produto: "))
desconto = preco*0.05
precof = preco-desconto
print(f"O preço do produto com 5% de desconto é de R$ {precof:.2f} ")
