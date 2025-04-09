#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.
metros = float(input("valor em metros: "))
centimetro = metros*100
milimetros = metros*1000

print(f"{metros} metros equivalem à: {centimetro} centimetros, que equivalem à {milimetros} milimetros")
