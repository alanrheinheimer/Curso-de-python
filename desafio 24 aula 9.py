#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou
#não com o nome "SANTO".

cid = str(input("cidade que você nasceu: ")).strip()
print(cid[:5].upper() == "SANTO")
