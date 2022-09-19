salario_mensal = input("Digite seu salário:  ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Digite seu gasto mensal:  ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal*12
gasto_total = gasto_mensal*12

montante = salario_total - gasto_total

print (f'O seu montante é de {montante}')