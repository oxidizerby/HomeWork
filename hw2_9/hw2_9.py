lst = ['BYN', 'USD', 'EUR']
sum = float(input('Введите сумму: '))
inp = input(f'Введите валюту с которой конвертируем {lst}: ').upper()
out = input(f'Введите валюту в которую конвертируем {lst}: ').upper()

ex = {'BYNUSD': 0.5, 'USDBYN': 2, 'BYNEUR': 0.4, 'EURBYN': 2.5, 'USDEUR': 0.8, 'EURUSD': 1.25}

res = sum * ex[inp + out]
print(f"{sum} {inp} = {res:.2f} {out}")

# 1 USD = 2 BYN
# 1 EUR = 2.5 BYN
# 1 EUR = 1.25 USD

# USD = BYN * 0.5
# BYN = USD * 2

# EUR = BYN * 0.4
# BYN = EUR * 2.5

# EUR = USD * 0.8
# USD = EUR * 1.25
