from os import system
#a - move left
#d - move right
#s - stop the game


lenght          = 50
roboX           = 10
bombX           = 15
lifeX           = 19
money           = 12
roboX_battery   = 100
consumption     = 5
consuption_bomb = 50
additional_life = 40
total_money     = 10
steps           = 0
step            = 1



while True:
    system("cls")

#######################DRAWING THE MAP ### 
    x = 1
    print("\n")

    for x in range (lenght):
        if x == roboX:
            print("🤖", end = "")
        elif x == bombX:
            print("💣", end = "")
        elif x == lifeX:
            print("🧡", end = "")
        elif x == money:
            print("💰", end = "")
        else:
            print("●", end = "")
        x += 1
        
    print ("\n")
    steps += step
    if roboX == bombX:
        total_money -= 10
        print("You have lost 10 💰", total_money)
    else:
        total_money += 10
        print("You get + 10 💰", total_money) 
    if roboX == bombX:
        roboX_battery -= consuption_bomb
        print("You have lost 50 % and 10 💰 ")
    elif roboX == lifeX:
        roboX_battery += additional_life
        print("Congratulations! You get 40 % to your battery and 10 💰!")
    else:
        roboX_battery -= consumption
        print("Step:" , steps, "Charge: ", roboX_battery, "%")
        ##################ADDITIONAL##############
        if roboX <= 0 and roboX_battery > 0 :              
            print("YOUR GAME IS OVER", end = "")
            break
        ##########################################
    if roboX_battery <= 0:
        print("GAME IS OVER ")
        break
    #########ENDING OF DRAWING THE MAP################
    #########################CONTROLS#################
    direction = input("Enter the direction (a/d/s) >>>")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1
    if direction == "s":
        system ("cls")
        print("It was a good job!")
        break
    ############################
    


