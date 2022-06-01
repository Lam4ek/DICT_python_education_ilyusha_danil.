import random
a = random.choice([2,3,4,5,6,7,8,9])
b = random.choice([2,3,4,5,6,7,8,9])
operation = ['+','-','*']
c = random.choice(operation)
guess = (str(a) + c + str(b))
print (guess)
answer = int(input())
if c == '+':
    guess = a+b
if c == '-':
    guess = a-b
if c == '*':
    guess = a*b
if answer == guess:
    print('right!')
else:
    print('wrong!')
