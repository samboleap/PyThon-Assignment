future_value = float(input('Enter the desired future value :'))
rate = float(input('Enter the annual interest rate :'))
years = float(input('Enter the number of years the money will grow :'))
present_value = future_value / (1.0+rate)**years
print()