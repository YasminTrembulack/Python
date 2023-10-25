# 3 - Abaixo temos uma lista de times e suas classificações, utilizando esta lista, crie outras três e
# desenvolva um programa que separe os times entre primeira, segunda e terceira divisão.
# Output

times = ['1_palmeiras','2_coritiba', '1_corinthians', '3_juventude', '2_fluminense', '3_bahia',
'1_cuiaba', '2_cascavel', '3_ponte preta', '2_parana clube', '3_volta redonda' ]

primeiro = []
segundo = []
terceiro = []

for time in times:
    
    if time[0] == '1':
        primeiro.append(time[2:].capitalize())
    elif time[0] == '2':
        segundo.append(time[2:].capitalize())
    elif time[0] == '3':
        terceiro.append(time[2:].capitalize())
    
print(f"Classificação: \n1 - {primeiro}\n2 - {segundo}\n3 - {terceiro}")
    