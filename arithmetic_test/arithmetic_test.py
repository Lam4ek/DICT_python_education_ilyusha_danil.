import random
attempts = 0
score = 0
i = True
difficulity = input('Which level do you want? Enter a number:' "\n" '1 - simple operations with numbers 2-9' "\n" '2 - integral squares of 11-29: ')
while i == True:
    if difficulity == '1':
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
    if difficulity == '2':
        a = random.choice([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
        print(a)
        answer = (input())
        corAnswer = a*a
        if answer.isnumeric():
            if int(answer) == corAnswer:
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

print("Your mark is " + str(score) + " /5. Would you like to save the result? Enter yes or no.")
forDownload = input()
if forDownload == 'yes':
    name = input('What is your name?')
    print('The results are saved in "results.txt".')
    my_file = open("results.txt", "w+")
    my_file.write(name + ': ' + str(score) + " /5 in level " + difficulity)