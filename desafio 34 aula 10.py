#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para
# os inferiores ou iguais, o aumento é de 15%.

salario = float(input("digite o salario do funcionario: ")) #definindo salario

#aumento para salarios superiores a 1250
aumentosup = salario*0.10

##aumento para salarios inferiores ou iguais a 1250
aumentoinf = salario*0.15

#condiçao salarios
if salario > 1250:
    print(f"seu aumento foi de {aumentosup:.2f}, seu novo salario é {salario+aumentosup}")
else:
    print(f"seu aumento foi de {aumentoinf}, seu novo salario é {salario+aumentoinf}")