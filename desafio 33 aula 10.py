#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("digite o numero 1: "))
n2 = float(input("digite o numero 2: "))
n3 = float(input("digite o numero 3: "))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f"o menor valor digitado foi: {menor} ")

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3<n2:
    maior = n3
print(f"o maior numero digitado foi: {maior}")

