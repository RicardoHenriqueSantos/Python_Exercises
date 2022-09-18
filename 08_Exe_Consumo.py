# DESCRIÇÃO
print()
print("/// CÁLCULO DE CONSUMO MÉDIO ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
distancia = float(input("Insira a distância percorrida: "))
combustivel = float(input("Insira o combustível gasto: "))

# CÁLCULO
combustivel_medio = distancia / combustivel

# RESULTADO
print()
print(f"O valor do combustível médio é de {combustivel_medio:.3f}")
