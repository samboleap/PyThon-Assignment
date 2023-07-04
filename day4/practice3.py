marks = []
for i in range(5):
    mark = int(input('Please input mark:'))
    marks.append(mark)
print(marks)

average = sum(marks) / len(marks)
print(average)