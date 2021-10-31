water = 400
milk = 540
CoffeeBeans = 120
DisposableCups = 9
money = 550
print("The coffee machine has:")
print(str(water) + " of water")
print(str(milk) + " of milk")
print(str(CoffeeBeans) + " of coffee beans")
print(str(DisposableCups) + " of disposable cups")
print(str(money) + " of money")

while True:
    a = input("Write action (buy, fill, take):") 
    if a == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        type_of_coffee = input()
        if type_of_coffee == "1":
            water -= 250
            CoffeeBeans -= 16
            DisposableCups -= 1
            money += 4
            print("The coffee machine has:")
            print(str(water) + " of water")
            print(str(milk) + " of milk")
            print(str(CoffeeBeans) + " of coffee beans")
            print(str(DisposableCups) + " of disposable cups")
            print(str(money) + " of money")
        if type_of_coffee == "2":
            water -= 350
            milk -=75
            CoffeeBeans -= 20
            DisposableCups -=1
            money += 7
            print("The coffee machine has:")
            print(str(water) + " of water")
            print(str(milk) + " of milk")
            print(str(CoffeeBeans) + " of coffee beans")
            print(str(DisposableCups) + " of disposable cups")
            print(str(money) + " of money")
        if type_of_coffee == "3":
            water -= 200
            milk -= 100
            CoffeeBeans -= 12
            DisposableCups -=1
            money += 6
            print("The coffee machine has:")
            print(str(water) + " of water")
            print(str(milk) + " of milk")
            print(str(CoffeeBeans) + " of coffee beans")
            print(str(DisposableCups) + " of disposable cups")
            print(str(money) + " of money")
    if a == "fill":
        water += int(input("Write how many ml of water you want to add:"))
        milk += int(input("Write how many ml of milk you want to add:"))
        CoffeeBeans += int(input("Write how many grams of coffee beans you want to add:"))
        DisposableCups += int(input("Write how many disposable coffee cups you want to add:"))
    if a == "take":
        print("I gave you " + str(money))
        money -= money
        print("The coffee machine has:")
        print(str(water) + " of water")
        print(str(milk) + " of milk")
        print(str(CoffeeBeans) + " of coffee beans")
        print(str(DisposableCups) + " of disposable cups")
        print(str(money) + " of money")

            