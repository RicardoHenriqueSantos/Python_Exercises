# DESCRIÇÃO
print()
print("///// CÁLCULO PARA VERIFACAR O NÍVEL DE GLICOSE E SEU STATUS /////")
print()

# SAUDAÇÃO
print("Ola!")
print()

# INSERÇÃO DE DADOS
medida = float(input("Insira a medida da glicose: "))

# CÁLCULO E RESULTADO
if medida > 140:
    print()
    print("Classificação: Diabetes")
elif (medida > 100) and (medida <= 140):
    print()
    print("Classificação: Elevado")
else:
    print()
    print("Classificação: Normal")
