# DESCRIÇÃO
print()
print("///// CÁLCULO CONVERSOR DE TEMPERATURA /////")
print()

# SAUDAÇÃO
print("Ola!")
print()

# INSERÇÃO DE DADOS
escolha = input("Insira a escala inicial que será covertida (C / F): ")
temperatura = float(input("Insira a temperatura: "))

# CÁLCULO E RESULTADO
if escolha == "C":
    temperatura = temperatura * 1.8 + 32
    print()
    print(f"Temperatura equivalente em Fahrenheit: {temperatura:.2f}")
elif escolha == "F":
    temperatura = (temperatura - 32) / 1.8
    print()
    print(f"Temperatura equivalente em Celsius: {temperatura:.2f}")
