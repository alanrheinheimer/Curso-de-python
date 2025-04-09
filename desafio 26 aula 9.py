#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).upper().strip()

#quantas vezes aparece letra a
print(f"a letra A aparece : {frase.count('A')} vezes.")

#em que posiçao ela aparece pela primeira vez:
print(f"a letra A aparece a primeira vez na posição: {frase.find('A')+1}")
print(f"a letra A aparece a primeira vez na posição: {frase.rfind('A')+1}")



