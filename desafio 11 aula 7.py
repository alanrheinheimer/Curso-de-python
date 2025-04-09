#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros
# , calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.
altura = float(input("altura: "))
largura = float(input("largura: "))
area = altura*largura
qt = area/2
print(f"a area da parede é de {area} m2, e irá precisa de {qt} litros de tinta ")