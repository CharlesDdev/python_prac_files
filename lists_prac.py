sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
price = 1.50
new_day = input("Enter number of lemonades sold this week: ")
sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2

sales.sort()
worst_day_prof = sales[0] * price
best_day_prof = sales[-1] * price

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined day profit:$ {best_day_prof + worst_day_prof}')