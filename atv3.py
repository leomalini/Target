import json

with open('dados.json') as json_file:
    faturamento = json.load(json_file)

total_faturamento = sum([dia['valor'] for dia in faturamento])
media_faturamento = total_faturamento / len(faturamento)

menor_faturamento = min([dia['valor'] for dia in faturamento])
maior_faturamento = max([dia['valor'] for dia in faturamento])

dias_acima_da_media = sum([dia['valor'] > media_faturamento for dia in faturamento])

print(f"Menor faturamento do mês: {menor_faturamento}")
print(f"Maior faturamento do mês: {maior_faturamento}")
print(f"Média: {media_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
