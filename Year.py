current_year  = 2022
date_of_birth = int(input('Write the year of your birth '))
your_age      = current_year - date_of_birth
if 1900 <= date_of_birth and current_year >= date_of_birth :
    print('You are', your_age,'years old')
else:
    print('Error')
if  your_age >= 1 and your_age <3:
    print('You are baby')
elif your_age >= 4 and your_age < 9 :
    print('You are kid')
elif your_age >= 10 and your_age < 15:
    print('You are teen')
elif your_age >= 16 and your_age < 18 :
    print('You are young')
elif your_age >= 19 and your_age < 50:
    print('You are adult')
else:
    print('You are old') 

   





   



