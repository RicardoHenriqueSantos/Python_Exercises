# DESCRIÇÃO
print()
print("/// CÁLCULO DO VALOR DO PAGAMENTO DOS FUNCIONÁRIOS ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
print("Dados do funcionário: ")
nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
quantidade_hora = int(input("Quantidade de horas trabalhadas: "))

# CÁLCULO
pagamento = valor_hora * quantidade_hora

# RESULTADO
print()
print(f"O valor total a ser pago para {nome} é de R$ {pagamento:.2f}")