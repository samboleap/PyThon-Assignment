def total(*nubmers):
    sum = 0
    for number in nubmers:
        sum = sum + number

    return sum

student_a = total(60, 70, 65)
print(student_a)