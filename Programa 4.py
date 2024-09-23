### Programa 4
fatEstados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG' : 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total = sum(fatEstados.values())

for estado, valor in fatEstados.items():
    perc = valor * 100 / total
    print(f'{estado} = {perc:.2f}%')