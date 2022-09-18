# DESCRIÇÃO
print()
print("/// CÁLCULO DO TROCO DA MERCADORIA COMPRADA ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
preco = float(input("Insira o preço do produto: "))
quantidade = int(input("Insira a quantidade: "))
valor_recebido = float(input("Insira o valor recebido: "))

# CÁLCULO
valor_compra = preco * quantidade
troco = valor_recebido - valor_compra

# RESULTADO
print()
print(f"Valor da Compra R$ {valor_compra:.2f}")
print(f"Valor recebido R$ {valor_recebido:.2f}")
print(f"Troco R$ {troco:.2f}")