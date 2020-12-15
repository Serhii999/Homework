size = str(input("Write your size "))
bel_size = {'Russia': [42, 44, 46, 48, 50, 52, 54, 56],
            'Germany': [36, 38, 40, 42, 44, 46, 48, 50],
            'USA': [8, 10, 12, 14, 16, 18, 20, 22],
            'France': [38, 40, 42, 44, 46, 48, 50, 52],
            'Britain': [24, 26, 28, 30, 32, 34, 36, 38]}
def mejnar (dict):
    for country, razmeri in dict.items():
        if size == 'xxs':
            print (country, razmeri[0])
        elif size == 'xs':
            print (country, razmeri[1])
        elif size == 's':
            print(country, razmeri[2])
        elif size == 'm':
            print (country, razmeri[3])
        elif size == 'l':
            print (country, razmeri[4])
        elif size == 'xl':
            print (country, razmeri[5])
        elif size == 'xxl':
            print(country, razmeri[6])
        elif size == 'xxxl':
            print (country, razmeri[7])
    return('↑ These were the sizes in other countries')

print(mejnar(bel_size))


