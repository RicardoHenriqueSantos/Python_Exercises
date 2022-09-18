# DESCRIÇÃO DO PROBLEMA
print()
print("/// CÁLCULO DA MÉDIA DAS IDADES ///")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
print("Dados da 1º Pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))
print()

print("Dados da 2° Pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))
print()

# CÁLCULO
media = float((idade1 + idade2)/2)

# RESULTADO
print()
print(f"A média de idade de {nome1} e {nome2} é {media:.1f}")
