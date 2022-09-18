import math

# DESCRIÇÃO
print()
print("/// CÁLCULO DA FÓRMULA DE BASKARA PARA OS COEFICIENTES INSERIDOS ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

# CÁLCULOS E RESULTADOS
delta = (b**2) - (4 * a * c)

if delta < 0:
    print()
    print("A equação não possui raízes reais!")
    print()
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print()
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")
    print()



