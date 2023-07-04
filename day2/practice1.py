loanAmount = float(input("Enter the loan amount : "))
i = float(input("Enter the interest rate : "))
n = float(input("How mamny years to pay the loan : "))
i = i/12
n = n*12
Total = loanAmount* (i*(1+i)**n)/((1+i)**n-1)
print("This is the total payment :",("$"),Total,)
