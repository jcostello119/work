item_name = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))
total_cost = item_price * item_quantity

print('\nRECEIPT')
print(item_quantity, item_name, '@', '${:.2f}'.format(item_price), '=', '${:.2f}'.format(total_cost))
print('Total cost:', '${:.2f}'.format(total_cost),'\n')

second_item_name = input('Enter second food item name:\n')
second_item_price = float(input('Enter item price:\n'))
second_item_quantity = int(input('Enter item quantity:\n'))
second_total_cost = second_item_price * second_item_quantity

print('\nRECEIPT')
print(item_quantity, item_name, '@', '${:.2f}'.format(item_price), '=', '${:.2f}'.format(total_cost))
print(second_item_quantity, second_item_name, '@', '${:.2f}'.format(second_item_price), '=', '${:.2f}'.format(second_total_cost), '\n')
