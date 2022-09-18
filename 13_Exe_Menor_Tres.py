# DESCRIÇÃO
print()
print("/// INFORMAR O MENOR DOS TRÊS NÚMEROS DIGITADOS ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

# DEFINIÇÃO
if n1 < n2 and n1 < n3:
    print()
    print(f"O menor dos três é {n1}")
    print()
elif n2 < n1 and n2 < n3:
    print()
    print(f"O menor dos três é {n2}")
    print()
else:
    print()
    print(f"O menor dos três é {n3}")
    print()
