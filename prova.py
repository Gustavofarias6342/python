def calcular_media_ponderada(prova1, prova2, trabalho):
    # Pesos das notas
    peso_prova1 = 0.35
    peso_prova2 = 0.35
    peso_trabalho = 0.30

    # Cálculo da média ponderada
    media = (prova1 * peso_prova1) + (prova2 * peso_prova2) + (trabalho * peso_trabalho)

    return media

def verificar_situacao(media):
    if media >= 5.0:
        return "Aprovado"
    elif media >= 3.5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    nome = input("Digite o nome da pessoa: ")
    prova1 = float(input("Digite a nota da prova 1: "))
    prova2 = float(input("Digite a nota da prova 2: "))
    trabalho = float(input("Digite a nota do trabalho: "))

    media = calcular_media_ponderada(prova1, prova2, trabalho)
    situacao = verificar_situacao(media)

    print(f"A média de {nome} é: {media:.2f}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()
