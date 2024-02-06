anterior = float('inf')  # Definindo o valor inicial do número anterior como infinito

while True:
    numero = int(input("Digite um número inteiro: "))
    
    if numero < anterior:  # Verifica se o número atual é menor que o anterior
        print("O número atual é menor que o anterior. Encerrando o programa.")
        break  # Sai do loop se o número atual for menor que o anterior
    
    anterior = numero  # Atualiza o número anterior para o número atual

