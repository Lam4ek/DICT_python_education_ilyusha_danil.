import random
attempts = 0
score = 0
i = True
while i == True:
    a = random.choice([2,3,4,5,6,7,8,9])
    b = random.choice([2,3,4,5,6,7,8,9])
    operation = ['+','-','*']
    c = random.choice(operation)
    print (str(a) + c + str(b))
    answer = (input())
    if answer.isnumeric(): 
        if c == '+':
            guess = a+b
        if c == '-':
            guess = a-b
        if c == '*':
            guess = a*b
        if int(answer) == guess:
            print('right!')
            attempts = attempts+1
            score=score+1
        else:
            print('wrong!')
            attempts=attempts+1
        if attempts == 5:
            i=False
    else:
        print("incorect fornat")
print("Your mark is " + str(score) + " /5.")
