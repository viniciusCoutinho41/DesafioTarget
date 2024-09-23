### Programa 3
import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

fatPositivo = [dados['valor'] for dados in faturamento if dados['valor'] > 0]

menor = min(fatPositivo)
maior = max(fatPositivo)
media = sum(fatPositivo)/len(fatPositivo)
sup = sum(1 for valor in fatPositivo if valor > media)

print(f'O menor valor de faturamento no mês foi de: {menor}')
print(f'O maior valor de faturamento no mês foi de: {maior}')
print(f'O número de dias em que o faturamento foi superior a média mensal é de: {sup}')