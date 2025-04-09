#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em
# graus Celsius e converta para graus Fahrenheit.
tc = float(input("qual a temperatura em graus celcius?"))
tf = (tc*(9/5))+32
print(f"{tc} C equivalem a {tf} F")