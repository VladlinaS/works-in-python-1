food_1_name         = 'Pizza'
food_1_price        = 100
food_1_available    = 5
food_2_name         = 'Salat'
food_2_price        = 90
food_2_available    = 8
drink_1_name        = 'Sprite'
drink_1_price       = 30
drink_1_available   = 10
delivery_free_limit = 1000

food_1_quantity  = int (input('How many' + food_1_name  + 'do you want?'))
food_2_quantity  = int (input('How many portions of' +  food_2_name  + 'do you want?'))
drink_1_quantity = int (input('How many bottles of' +  drink_1_name  +  'do you want? '))
food_1_cost      = food_1_quantity * food_1_price
food_2_cost      = food_2_quantity * food_2_price
drink_1_cost     = drink_1_quantity * drink_1_price
food_total_cost  =  food_1_cost + food_2_cost + drink_1_cost
delivery_wanted_str = input('Do you want delivery (Yes/No) ?')

if food_1_quantity <= 5:
    print ('You have ordered', food_1_quantity, food_1_name)
else:
    print ('You can order only', food_1_available, food_1_name)
if food_2_quantity <= 8:
    print('You have ordered', food_2_quantity, food_2_name )
else:
    print('You can order only', food_2_available, food_2_name)
if drink_1_quantity <= 10:
    print('You have ordered', drink_1_quantity, drink_1_name)
else:
    print('You can order only', drink_1_available, drink_1_name)
if food_1_quantity > 5 and food_2_quantity > 8 and drink_1_quantity > 10:
    print('You can not make an order for so many products ')
else:
    print('You have ordered', food_1_quantity,'*', food_1_name,'+', food_2_quantity,'*', food_2_name, '+', drink_1_quantity, '*', drink_1_name, '=', food_total_cost, "Lei")
if food_1_quantity > 5 and food_2_quantity > 8 and drink_1_quantity > 10:
     print('Delivery is not available')
elif food_total_cost > 1000 and delivery_wanted_str== 'Yes':
    print('You have free delivery')
elif delivery_wanted_str == 'No':
    print('You do not have delivery ')
else:
    print('You have to pay for delivery - 150 Lei')