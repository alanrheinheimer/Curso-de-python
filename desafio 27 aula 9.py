#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

#solicitando nome completo:
nome = str(input("digite seu nome: "))

#achando o primeiro nome
primeiro_nome = nome.split()[0]

print(f"o seu primeiro nome é: {primeiro_nome}")

#achando ultimo nome:

segundo_nome = nome.split()[-1]

print(f"seu ultimo nome é: {segundo_nome}")
