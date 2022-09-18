# DESCRIÇÃO
print()
print("///// CÁLCULO DO LANCHE COMPRADO /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
codigo = float(input("Insira o código do produto: "))
quantidade = int(input("Insira a quantidade: "))

# CÁLCULO E RESULTADO
if codigo == 1:
    valor = 5.00 * quantidade
    print()
    print(f"Valor a pagar: R$ {valor:.2f}")
elif codigo == 2:
    valor = 3.50 * quantidade
    print()
    print(f"Valor a pagar: R$ {valor:.2f}")
elif codigo == 3:
    valor = 4.80 * quantidade
    print()
    print(f"Valor a pagar: R$ {valor:.2f}")
elif codigo == 4:
    valor = 8.90 * quantidade
    print()
    print(f"Valor a pagar: R$ {valor:.2f}")
else:
    valor = 7.32 * quantidade
    print()
    print(f"Valor a pagar: R$ {valor:.2f}")
