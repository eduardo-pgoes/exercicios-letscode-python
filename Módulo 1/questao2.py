# Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;
# O programa deve imprimir uma mensagem de erro para cada informação
# inválida.

# Verificação da idade
while True:
    try:
        idade = int(input("Insira sua idade: "))
        if idade < 150 and idade > 0:
            break
        else:
            print("Valor inválido para a idade.")
    except ValueError:
        print("A idade não é um inteiro!")
        
# Verificação do salário
while True:
    try:
        salario = float(input("Insira seu salário: R$ "))
        if salario > 0:
            break
        else:
            print("O salário deve ser não-negativo.")
    except ValueError:
        print("O salário não é um número!")

# Verificação do sexo
sexos_permitidos = ["M", "F", "Outro"]
while True:
    sexo = input("Insira seu sexo (M, F ou Outro): ")
    if sexo in sexos_permitidos:
        break
    else:
        print("O sexo inserido não está dentro das opções permitidas.")