def total(a,b,c):
    total = a + b +c 
    return total

math = float(input('Enter your math: '))
eng = float(input('Enter your eng: '))
physic = float(input('Enter your physic: '))

#call function for total the marks\
all_marks = total (math, eng, physic)

print(all_marks)