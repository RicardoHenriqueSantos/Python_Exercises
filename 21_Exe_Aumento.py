# DESCRIÇÃO
print()
print("///// CÁLCULO DE AUMENTO CORRESPONTE AO SALÁRIO /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
salario = float(input("Insira o salário atual: "))
print()

# CÁLCULO E RESULTADOS
if salario <= 1000:
    aumento = salario * 0.20
    atual = salario + aumento
    print(f"Novo salário: R$ {atual:.2f}")
    print(f"Aumento: R$ {aumento:.2f}")
    print("Porcentagem 20%")
elif 1000 < salario <= 3000:
    aumento = salario * 0.15
    atual = salario + aumento
    print(f"Novo salário: R$ {atual:.2f}")
    print(f"Aumento: R$ {aumento:.2f}")
    print("Porcentagem 15%")
elif 3000 < salario <= 8000:
    aumento = salario * 0.10
    atual = salario + aumento
    print(f"Novo salário: R$ {atual:.2f}")
    print(f"Aumento: R$ {aumento:.2f}")
    print("Porcentagem 10%")
else:
    aumento = salario * 0.05
    atual = salario + aumento
    print(f"Novo salário: R$ {atual:.2f}")
    print(f"Aumento: R$ {aumento:.2f}")
    print("Porcentagem 5%")
