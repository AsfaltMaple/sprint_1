world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for key, value in world_champions.items():
    years = world_champions.keys()
    countries = world_champions.values()
    print(f'{key} - {value}')

if 'Италия' in countries:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else: print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')




#    for year, country in world_champions.items():
 #       if country == 'Италия':
  #          print(year)
