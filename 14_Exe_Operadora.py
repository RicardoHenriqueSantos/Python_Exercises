# DESCRIÇÃO
print()
print("/// CÁLCULO PARA INFORMAR O VALOR A SER PAGO CONSUMIDO ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
duracao = int(input("Insira a quantidade de minutos consumidos: "))

# CÁLCULO E RESULTADO
if duracao <= 100:
    print()
    print("O valor a ser pago é de R$ 50.00")
    print()
else:
    minutos = duracao - 100
    valor = float(50 + (minutos * 2))

    print()
    print(f"O valor a ser pago é de R$ {valor:.2f}")
    print()
