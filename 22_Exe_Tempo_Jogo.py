# DESCRIÇÃO
print()
print("///// CÁLCULO TEMPO TOTAL DE JOGO /////")
print()

# SAUDAÇÃO
print("Olá!")
print()

# INSERÇÃO DE DADOS
inicial = int(input("Insira a hora inicial: "))
final = int(input("Insira a hora final: "))

# CÁLCULO E RESULTADO

if inicial == final:
    print()
    print("O JOGO DUROU 24 HORAS!")

elif final > inicial:
    print()
    tempo = final - inicial
    print(f"O JOGO DUROU {tempo} HORAS!")
else:
    print()
    tempo = 24 - inicial
    tempo = tempo + final
    print(f"O JOGO DUROU {tempo} HORAS!")
