conicoins = int(input("Please, enter the number of conicoins you have: "))
xrate = float(input("Please, enter the exchange rate: "))
result = conicoins*xrate
if 2*result % 2 == 0:
    result = int(result)
print(f"The total amount of dollars: {result}")
