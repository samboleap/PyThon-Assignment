total_pen = 8
total_book = 6 
pen_price = 4
book_price = 8 
book_remain = 4
pen_remain = 4

pen_sold = total_pen - pen_remain
pen_income= pen_sold*pen_price

book_sold = total_book - book_remain
book_income = book_sold*book_price

print("Income from selling pen is : ", pen_income)
print("Income from selling book is: " , book_income)