water = 400
milk = 540
CoffeeBeans = 120
DisposableCups = 9
money = 550

while True:
    a = input("Write action (buy, fill, take, remaining, exit):") 
    if a == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        type_of_coffee = input()
        if type_of_coffee == "1":
            if water < 250:
                print("Sorry, not enough water!")
            elif CoffeeBeans < 16:
                print("Sorry, not enough Coffee Beans!")
            elif DisposableCups < 1:
                print("Sorry, not enough Disposable Cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 250
                CoffeeBeans -= 16
                DisposableCups -= 1
                money += 4

        if type_of_coffee == "2":
            if water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk")
            elif CoffeeBeans < 20:
                print("Sorry, not enough Coffee Beans!")
            elif DisposableCups < 1:
                print("Sorry, not enough Disposable Cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -=75
                CoffeeBeans -= 20
                DisposableCups -=1
                money += 7

        if type_of_coffee == "3":
            if water < 200:
                print("Sorry, not enough water!")
            elif milk < 100:
                print("Sorry, not enough milk")
            elif CoffeeBeans < 12:
                print("Sorry, not enough Coffee Beans!")
            elif DisposableCups < 1:
                print("Sorry, not enough Disposable Cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                CoffeeBeans -= 12
                DisposableCups -=1
                money += 6

    if a == "fill":
        water += int(input("Write how many ml of water you want to add:"))
        milk += int(input("Write how many ml of milk you want to add:"))
        CoffeeBeans += int(input("Write how many grams of coffee beans you want to add:"))
        DisposableCups += int(input("Write how many disposable coffee cups you want to add:"))
    if a == "take":
        print("I gave you " + str(money))
        money -= money
    if a == "remaining":
        print("The coffee machine has:")
        print(str(water) + " of water")
        print(str(milk) + " of milk")
        print(str(CoffeeBeans) + " of coffee beans")
        print(str(DisposableCups) + " of disposable cups")
        print(str(money) + " of money")
    if a == "exit":
        break


            