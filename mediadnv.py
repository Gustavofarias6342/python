# Função para calcular a média
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Função principal
def main():
    # Listas para armazenar os nomes e notas dos alunos
    nomes = []
    notas = []

    # Receber os dados dos alunos
    for i in range(3):
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nota = float(input("Digite a nota (0-10) do aluno {}: ".format(nome)))
        
        # Verificar se a nota está dentro do intervalo correto
        while nota < 0 or nota > 10:
            print("A nota deve estar entre 0 e 10.")
            nota = float(input("Digite novamente a nota (0-10) do aluno {}: ".format(nome)))

        # Adicionar o nome e a nota à lista
        nomes.append(nome)
        notas.append(nota)

    # Calcular as médias
    medias = [calcular_media(notas[0], notas[1], notas[2]) for notas in zip(*[notas[i::3] for i in range(3)])]

    # Encontrar o índice da maior média
    indice_maior_media = medias.index(max(medias))

    # Exibir o resultado na tela
    print("O aluno {} teve a maior média {:.2f}".format(nomes[indice_maior_media], medias[indice_maior_media]))

if __name__ == "__main__":
    main()
