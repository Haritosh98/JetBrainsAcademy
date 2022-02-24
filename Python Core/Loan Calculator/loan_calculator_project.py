import argparse
import math

parser = argparse.ArgumentParser(description="This program is a loan calculator")

parser.add_argument("--type", choices=["annuity", "diff"], action='store', type=str, help = 'Your input should be either "annuity" or "diff"')
parser.add_argument("--principal", action='store', type = float, help = 'This is the principal loan amount')
parser.add_argument("--periods", action='store', type = int, help = 'This is the number of payments, usually in months, to repay the loan')
parser.add_argument("--payment", action='store', type = float, help = 'This is the monthly payment amount a.k.a. annuity')
parser.add_argument("--interest", action='store', type = float, help = 'This is the interest (without the percentage sign)')

args = parser.parse_args()

Qu = args.type  # this is either 'annuity' or 'diff'. Input should be either "annuity" or "diff"
p = args.principal  # this is a floating point number. This is the principal loan amount
n = args.periods  # this is a int number. This is the number of payments, usually in months, to repay the loan
mp = args.payment  # this is a floating point number. This is the monthly payment amount a.k.a. annuity
i = args.interest  # this is a floating point number. This is the interest

if (i is None) or (type is None) or (type == 'diff' and mp is not None) or (n is not None and n < 0):
    print('Incorrect parameters.')
# elif p or n or mp or i < 0:
#     print('Variables must be positive.')

else:
    nir = (i / 100) / 12
    if Qu == 'diff' and p is not None and n is not None:
        ovp = 0
        for m in range(1, n + 1):
            Diff = p / n + nir * (p - (p * (m - 1)) / n)
            print(f'Month {m}: payment is {math.ceil(Diff)}')
            ovp += math.ceil(Diff)
        print(f'\nOverpayment = {math.ceil(ovp - p)}')

    elif Qu == 'annuity' and (p is not None) and (n is not None):
        mp = math.ceil(p * (nir * ((1 + nir) ** n)) / (((1 + nir) ** n) - 1))
        print('Your annuity payment = {}!'.format(mp))
        ovp = (mp * n - p)
        print(f'\nOverpayment = {math.ceil(ovp)}')

    elif Qu == 'annuity' and (p == None):
        p = 0  # To initialise p from None
        p = math.floor(mp / ((nir * ((1 + nir) ** n)) / (((1 + nir) ** n) - 1)))
        print (f'Your loan principal = {p}!')
        ovp = mp * n - p
        print(f'\nOverpayment = {math.ceil(ovp)}')

    elif Qu == 'annuity' and (n == None):
        n = 0  # To initialise n from None
        n = math.ceil (math.log((mp / (mp - (nir * p))), (1 + nir)))  # num of months
        years = n // 12
        months_remaining = n % 12
        if years == 0:
           print('It will take {} month{} to repay this loan!'.format(int(months_remaining), 's' if months_remaining > 1 else ''))
        elif months_remaining == 0:
            print('It will take {} year{} to repay this loan!'.format(int(years), 's' if years > 0 else ''))
        else:
            print('It will take {} year{} and {} month{} to repay this loan!'.format(int(years), 's' if years > 0 else '', int(months_remaining), 's' if months_remaining > 1 else ''))
        ovp = mp * n - p
        print(f'\nOverpayment = {math.ceil(ovp)}')
