# DESCRIÇÃO
print()
print("///// CÁLCULO PARA DEFINIÇÃO DE MAIOR DISTÂNCIA LANÇADA /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
print("Insira as três distâncias: ")
d1 = float(input())
d2 = float(input())
d3 = float(input())

# CÁLCULO E RESULTADO
if (d1 > d2) and (d1 > d3):
    print()
    print(f"Maior distância: {d1:.2f}")
elif (d2 > d1) and (d2 > d3):
    print()
    print(f"Maior distância: {d2:.2f}")
else:
    print()
    print(f"Maior distância: {d3:.2f}")
