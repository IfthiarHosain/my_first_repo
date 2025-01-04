numbers=[5,12,10,8,4,25]
squred_number=[square for num in numbers if (square := num**2) >100]
print(squred_number) 