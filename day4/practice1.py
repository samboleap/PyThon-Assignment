Standard_hour = 40

Total_hour = float(input("Enter the total hour : "))

Normal_rate = float(input("Enter the normal rate : "))
if Total_hour > 40 : 
    GT_hour = Total_hour - Standard_hour
    print("This is the GT_hour: ",GT_hour,"h")

    GT_wages = GT_hour * (Normal_rate*2)
    print("This is GT_wages: ",GT_wages,"$")
    
    Normal_wages = Standard_hour * Normal_rate
    print("This is Normal_wages: ",Normal_wages,"$")
    
    Gross_wages = Normal_wages+GT_wages
    print("This is Gross_wages: ",Gross_wages,"$")

else :

    Gross_wages = Total_hour * Normal_rate
    print("This is Gross_wages:" ,Gross_wages,"$") 
