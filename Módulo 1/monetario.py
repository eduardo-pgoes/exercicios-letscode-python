# Enunciado:
# Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
# programa deve imprimir a mensagem “O novo valor é [valor]”.

valor = float(input("Insira um valor: R$ "))
novo_valor = valor * 0.85
print("O novo valor é: R$", novo_valor)