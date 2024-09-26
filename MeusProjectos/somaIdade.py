idades = [14, 15, 17, 18, 15]
total = 0
for idade in idades:
    total += idade
    media = total / len(idades)
print(f'A soma de todas ass idade da lista é de: {total}')
print(f'A media de todas das {len(idades)} idade da lista é de: {media}')