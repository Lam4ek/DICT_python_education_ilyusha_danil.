bot_name = ("Lam4ek")
birth_year = ("2021")
print("Hello! My name is" + " " + bot_name)
print("I was created in" + " " + birth_year)
print("Please, remind me your name.")
your_name = input(str())
print("What a great name you have," + " " + your_name + "!")
print("Let me guess your age.") 
print("Enter remainders of dividing your age by 3, 5 and 7.")
a = int(input())
b = int(input())
c = int(input())
your_age = (a*70+b*21+c*15) % 105
print("Your age is" + " " + str(your_age) + ";" + " " + "that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
i = -1
d = "!"
your_number = int(input())
while i < your_number:
    i = i+1
    print (str(i) + "!")
print("Completed, have a nice day!")