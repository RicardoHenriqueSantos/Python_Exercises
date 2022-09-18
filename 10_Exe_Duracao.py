# DESCRIÇÃO
print()
print("/// CÁLCULO PARA FORMATAÇÃO DE CRONÔMETRO ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
duracao = int(input("Insira o número de segundos a serem calculados: "))

# CÁLCULO
hora = duracao // 3600
resto = duracao % 3600
minuto = int(resto / 60)
segundo = resto % 60

# RESULTADO
print()
print(f"{hora}:{minuto}:{segundo}")
