girabola = ('Pedro de Luanda','Sagrada Esperança','1º de Agosto',
'Primeiro de Agosto','Interclube','Wiliete de Benguela','Académica do Lobito',
'Kabuscorp','Bravos do Maquis','Desportivo da Huíla','Recreativo do Libolo',
'Santa Rita de Cássia','Jovens do Palanca','Progresso do Sambizanga','Atlético Petróleos do Huambo')
print(f'A) Os 5 primeiros do Campionato: {girabola[:5]}')
print(f'B) Os 4 ultimo do Campeonato: {girabola[-4:]}')
print(f'C) Times por ordem Alfabetica: {sorted(girabola)}')
print(f'{girabola[5]} Esta na posição {len(girabola) - len(girabola[5:])}')