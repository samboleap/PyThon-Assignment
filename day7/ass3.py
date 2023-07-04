loan_amount = int(input("Please input the loan amount that you borrow:"))
i = float(input("The interest rate (per year) of the bank: "))
n = int(input("How many year to pay the loan: "))

i = i/12; #interest per month
n = n*12; #number of time 12 times per year 

total_payment = loan_amount*( (i*(1+i)**n)/ ((1+i)**n-1))

print("The amount to pay every month is: ", total_payment)
