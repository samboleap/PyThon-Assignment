def total(a, b, c):

    sum = a + b + c

    return sum

math = int(input("Please input mark for math:"))
eng = int(input("Please input mark for math:"))
physic = int(input("Please input mark for math:"))

#call function for total the marks
#all_mark = total(20, 30, 40)

all_mark = total(math, eng, physic)

print(all_mark)