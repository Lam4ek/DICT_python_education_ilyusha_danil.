class CoffeeMchine:
    def __init__(self, water, milk, CoffeeBeans, DisposableCups, money):
        self.water = water
        self.milk = milk
        self.CoffeeBeans = CoffeeBeans
        self.DisposableCups = DisposableCups
        self.money = money

    def buy_expresso(self):
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.CoffeeBeans < 16:
            print("Sorry, not enough Coffee Beans!")
        elif self.DisposableCups < 1:
            print("Sorry, not enough Disposable Cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.CoffeeBeans -= 16
            self.DisposableCups -= 1
            self.money += 4
        return self

    def buy_latte(self):
        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk")
        elif self.CoffeeBeans < 20:
            print("Sorry, not enough Coffee Beans!")
        elif self.DisposableCups < 1:
            print("Sorry, not enough Disposable Cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -=75
            self.CoffeeBeans -= 20
            self.DisposableCups -=1
            self.money += 7
        return self
    
    def buy_cappucino(self):
        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk")
        elif self.CoffeeBeans < 12:
            print("Sorry, not enough Coffee Beans!")
        elif self.DisposableCups < 1:
            print("Sorry, not enough Disposable Cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.CoffeeBeans -= 12
            self.DisposableCups -=1
            self.money += 6
        return self
    
    def fill(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.CoffeeBeans += int(input("Write how many grams of coffee beans you want to add:"))
        self.DisposableCups += int(input("Write how many disposable coffee cups you want to add:"))
        return self
    
    def take(self):
        print("I gave you " + str(self.money))
        self.money -= self.money
        return self
    
    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.CoffeeBeans) + " of coffee beans")
        print(str(self.DisposableCups) + " of disposable cups")
        print(str(self.money) + " of money")

CF = CoffeeMchine(400, 540, 120, 9, 550)
while True:
    a = input("Write action (buy, fill, take, remaining, exit):")
    if a == "buy":
        action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        if action == "1":
            CF.buy_expresso()
        if action == "2":
            CF.buy_latte()
        if action == "3":
            CF.buy_cappucino()
        if action == "back":
            continue
    elif a == "fill":
        CF.fill()
    elif a == "take":
        CF.take()
    elif a == "remaining":
        CF.remaining()
    elif a == "exit":
        break
    else:
        print("wrong command")


        






        



    # def buy(self):
    #     if a == "buy":
    #         print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    #         type_of_coffee = input()
    #         if type_of_coffee == "1":
    #             if self.water < 250:
    #                 print("Sorry, not enough water!")
    #             elif self.CoffeeBeans < 16:
    #                 print("Sorry, not enough Coffee Beans!")
    #             elif self.DisposableCups < 1:
    #                 print("Sorry, not enough Disposable Cups!")
    #             else:
    #                 print("I have enough resources, making you a coffee!")
    #                 self.water -= 250
    #                 self.CoffeeBeans -= 16
    #                 self.DisposableCups -= 1
    #                 self.money += 4

    #         if type_of_coffee == "2":
    #             if self.water < 350:
    #                 print("Sorry, not enough water!")
    #             elif self.milk < 75:
    #                 print("Sorry, not enough milk")
    #             elif self.CoffeeBeans < 20:
    #                 print("Sorry, not enough Coffee Beans!")
    #             elif self.DisposableCups < 1:
    #                 print("Sorry, not enough Disposable Cups!")
    #             else:
    #                 print("I have enough resources, making you a coffee!")
    #                 self.water -= 350
    #                 self.milk -=75
    #                 self.CoffeeBeans -= 20
    #                 self.DisposableCups -=1
    #                 self.money += 7

    #         if type_of_coffee == "3":
    #             if self.water < 200:
    #                 print("Sorry, not enough water!")
    #             elif self.milk < 100:
    #                 print("Sorry, not enough milk")
    #             elif self.CoffeeBeans < 12:
    #                 print("Sorry, not enough Coffee Beans!")
    #             elif self.DisposableCups < 1:
    #                 print("Sorry, not enough Disposable Cups!")
    #             else:
    #                 print("I have enough resources, making you a coffee!")
    #                 self.water -= 200
    #                 self.milk -= 100
    #                 self.CoffeeBeans -= 12
    #                 self.DisposableCups -=1
    #                 self.money += 6
    # def fill(self):
    #     if a == "fill":
    #         self.water += int(input("Write how many ml of water you want to add:"))
    #         self.milk += int(input("Write how many ml of milk you want to add:"))
    #         self.CoffeeBeans += int(input("Write how many grams of coffee beans you want to add:"))
    #         self.DisposableCups += int(input("Write how many disposable coffee cups you want to add:"))
    # def take(self):        
    #     if a == "take":
    #         print("I gave you " + str(money))
    #         self.money -= self.money
    # def remaining(self):        
    #     if a == "remaining":
    #         print("The coffee machine has:")
    #         print(str(self.water) + " of water")
    #         print(str(self.milk) + " of milk")
    #         print(str(self.CoffeeBeans) + " of coffee beans")
    #         print(str(self.DisposableCups) + " of disposable cups")
    #         print(str(self.money) + " of money")

