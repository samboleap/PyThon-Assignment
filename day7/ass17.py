# program to calculate the sum of numbers
# until the user enters zero
total = 0 
number = int(input('Enter a number: '))

while number != 0:
    total += number     #total = total + number

    # take integer input again
    number = int(input('Enter a number: '))
print('total = ', total)