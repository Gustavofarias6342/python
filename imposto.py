def calcular_irpf(renda_anual):
    if renda_anual <= 22847.76:
        imposto = 0
    elif 22847.77 <= renda_anual <= 33919.80:
        imposto = (renda_anual * 0.075) - 1713.58
    elif 33919.81 <= renda_anual <= 45012.60:
        imposto = (renda_anual * 0.15) - 4257.57
    elif 45012.61 <= renda_anual <= 55976.16:
        imposto = (renda_anual * 0.225) - 7633.51
    else:
        imposto = (renda_anual * 0.275) - 10432.32
    
    return imposto

renda_anual = float(input("Digite sua renda anual: "))
imposto_a_pagar = calcular_irpf(renda_anual)
print("O imposto de renda a pagar é:", imposto_a_pagar)
