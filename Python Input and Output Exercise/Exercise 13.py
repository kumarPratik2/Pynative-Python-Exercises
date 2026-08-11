#Display a large number as currency, including a dollar sign, commas for thousands, and two decimal places.

Amount = 1250500.7

result = f'${Amount:,.2f}'
print(f'Total Balance:{result}')