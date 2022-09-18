# DESCRIÇÃO
print()
print("/// CÁLCULO PARA AVALIAR MÉDIA E SITUAÇÃO DOS ALUNOS ///")
print()

# SAUDAÇÃO
print("Ola!")
print()

# INSERÇÃO DOS DADOS
nome = input("Insira o nome do aluno: ")
nota1 = float(input("Insira a Nota 1: "))
nota2 = float(input("Insira a Nota 2: "))

media = (nota1 + nota2) / 2

# CÁLCULOS E RESULTADOS
if media > 60:
    print()
    print(f"Média: {media:.2f}")
    print(f"Situação: APROVADO")
    print()
else:
    print()
    print(f"Média: {media:.2f}")
    print(f"Situação: REPROVADO")
    print()
