# DESCRIÇÃO
print()
print("///// CÁLCULO DE COORDENADAS /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
print(" Q2 | Q1")
print(" ---|---")
print(" Q3 | Q4")
print()
x = float(input("Insira o valor de X: "))
y = float(input("Insira o valor de y: "))
print()

# CÁLCULO E RESULTADO
if x == 0 and y == 0:
    print("Origem")
elif x == 0 and y != 0:
    print("Eixo Y")
elif y == 0 and x != 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")