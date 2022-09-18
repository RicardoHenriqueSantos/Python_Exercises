# DESCRIÇÃO
print()
print("///// CÁLCULO PARA INFORMAR SE NÚMEROS SÃO MÚLTIPLOS /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
print("Insira dois números: ")
n1 = int(input())
n2 = int(input())

# CÁLCULO E RESULTADO
if (n1 % n2 == 0) or (n2 % n1 == 0):
    print()
    print("Os números são múltiplos.")
else:
    print()
    print("Os números não são múltiplos.")
