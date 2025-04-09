#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.
salario = float(input("salario do funcionario: "))
aumento = salario*0.15
salarionovo = salario+aumento
print(f"o novo salário é R$ {salarionovo:.2f}")
