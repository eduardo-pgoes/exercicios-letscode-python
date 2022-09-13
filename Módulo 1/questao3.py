# Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir o assassino, a polícia faz um pequeno questionário com 5
# perguntas onde a resposta só pode ser sim ou não:
# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
# suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
# 2 pontos são apenas suspeitos, necessitando outras investigações. Valores
# iguais ou abaixo de 1 são liberados

respostas_permitidas = ["S", "N"]
pontuacao = 0 
perguntas = ["Mora perto da vítima?", "Já trabalhou com a vítima?", "Telefonou para a vítima?", "Esteve no local do crime?",
            "Devia para a vítima?"]

for pergunta in perguntas:
    while True:
        resposta = input('{0} (S/N) '.format(pergunta)).upper()
        if resposta in respostas_permitidas:
            if resposta == "S":
                pontuacao += 1
            break
        else:
            print("Resposta inválida!")

if pontuacao == 5:
    print("Você é o assassino!")
elif pontuacao >= 3:
    print("Você é cúmplice...")
elif pontuacao >= 2:
    print("Você é suspeito!")
else:
    print("Você foi liberado.")