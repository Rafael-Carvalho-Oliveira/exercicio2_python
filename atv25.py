#INFORMANDO A TAXA, CAPITAL E TEMPO
taxa = int(input("Informe a taxa dos juros: "))
capital = int(input("Informe o capital: "))
tempo = int(input("Informe o tempo: "))
#O CÁLCULO DE JUROS
juros = capital*taxa*tempo
#E O RESULTADO
print(f"O valor dos juros simples será: {juros}")