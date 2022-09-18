# DESCRIÇÃO
print()
print("/// CÁLCULO DE VERIFICAÇÃO DE TROCO ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS E CÁLCULO
valor = float(input("Valor do produto: "))
quantidade = int(input("Quantidade adquirida: "))
total = valor * quantidade

print(f"Valor total da compra R$ {total:.2f}")

print()
recebido = float(input("Insira o valor recebido: "))

# RESULTADO
if recebido > total:
    print()
    troco = recebido - total
    print(f"Troco R$ {troco:.2f}")
else:
    print()
    restante = total - recebido
    print(f"Restante a ser pago R$ {restante:.2f}")
