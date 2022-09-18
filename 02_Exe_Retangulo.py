import math

# DESCRIÇÃO DO PROBLEMA
print()
print("/// CÁLCULO DA ÁREA, PERÍMETRO E DIAGONAL DE UM RETÂNGULO ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))

# CÁLCULOS
area = base * altura
perimetro = (base + altura) * 2
diagonal = math.sqrt(base**2 + altura**2)

# RESULTADOS
print()
print(f"Área = {area:.4f}")
print(f"Perimetro {perimetro:.4f}")
print(f"Diagonal {diagonal:.4f}")