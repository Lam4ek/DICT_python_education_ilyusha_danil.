print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
water = 200
milk = 50
CoffeeBeans = 15

# print("For 25 cups of coffee you will need:")
# print(str(cups * water) + "ml of water") 
# print(str(cups * milk) + "ml of milk")
# print(str(cups * CoffeeBeans) + "g of coffee beans")

amount_of_water = int(input("Write how many ml of water the coffee machine has:"))
amout_of_milk = int(input("Write how many ml of milk the coffee machine has:"))
amout_of_CoffeeBeans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))

PossibleAmount = min(amount_of_water //  water, amout_of_milk // milk, amout_of_CoffeeBeans // CoffeeBeans)

if PossibleAmount >= cups:
    print("Yes, I can make that amount of coffee(and even " + str(PossibleAmount - cups) + " more than that)")
else:
    print("No, I can make only " + str(PossibleAmount) + " cups of coffee")
    