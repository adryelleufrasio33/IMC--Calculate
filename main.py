try:
    nome = input("Digite seu nome: ").strip()
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
except ValueError:
    print("Erro: peso e altura devem ser números.")
    exit()

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

imc = calcular_imc(peso, altura)


if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
     print("Peso normal")
elif 25 < imc < 29.9:
     print("Sobrepeso")
elif  30 <= imc <= 34.9 :
    print("Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade Grau II (severa)")
else:
    print("Morbida")

print(f"Seu nome é {nome}, Sua altura é {altura}, Seu peso é {peso}, e o resultado do seu imc é {imc:.2f}")
     
