# DESCRIÇÃO
print()
print("/// CÁLCULO DE ÁREA DAS MEDIADAS ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
a = float(input("Insira a medida A: "))
b = float(input("Insira a medida B: "))
c = float(input("Insira a medida C: "))

# CÁLCULO
area_quadrado = a * a
area_triangulo = (a * b)/2
area_trapezio = ((a + b)*c)/2

# RESULTADO
print()
print(f"Área do quadrado: {area_quadrado:.3f}")
print(f"Área do triângulo: {area_triangulo:.3f}")
print(f"Área do trapézio: {area_trapezio:.3f}")
