KPI = 1000

nome = input("Escreva o seu nome: ")

salario = float(input("Digite o valor do seu salario: "))

bonus = float(input("Digite o valor do bonus recebido: "))

bonus_final = KPI + salario * bonus

print(f"O usuario {nome} possui o bonus de {bonus_final}")