
def calcular_imc(peso, altura):
    return peso * (altura * altura)  # Fórmula errada


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    return "Obesidade"

peso = 70
altura = 1.75
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}, Classificação: {classificar_imc(imc)}")
