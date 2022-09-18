# DESCRIÇÃO DO PROBLEMA
print("")
print("/// CÁLCULO DO VALOR E ÁREA DO TERRENO ///")
print("")

# SAUDAÇÃO
print("Olá!")
print("")

# INSERÇÃO DE DADOS
altura = float(input("Insira a altura do terreno: "))
largura = float(input("Insira a largura do terreno: "))
valor_m2 = float(input("Insira o valor do metro quadrado: "))

# CÁLCULOS
area_terreno = altura * largura
valor_terreno = area_terreno * valor_m2

# RESULTADOS
print("")
print(f"Área do terreno = {area_terreno:.2f}")
print(f"O valor do terreno é R$ {valor_terreno:.2f}")
