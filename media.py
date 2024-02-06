def calcular_media(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

alunos = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota de {}: ".format(nome)))
    nota2 = float(input("Digite a segunda nota de {}: ".format(nome)))
    nota3 = float(input("Digite a terceira nota de {}: ".format(nome)))

    media = calcular_media(nome, nota1, nota2, nota3)
    alunos.append((nome, media))

aluno_com_maior_media = max(alunos, key=lambda x: x[1])

print("O aluno {} teve a maior média: {}".format(aluno_com_maior_media[0], aluno_com_maior_media[1]))
