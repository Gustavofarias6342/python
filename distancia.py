#programa distancia
origem = input("Cidade de origem: ")
destino = input("Cidade de desino: ")
distacia = float(input("Qual a distancia em km? "))
velocidade = float(input("quantos km/h irá viajar?"))
tempo = distacia/velocidade*60
print(f"Voce levara {tempo} minutos de {origem} á {destino}")