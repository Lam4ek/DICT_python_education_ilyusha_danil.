import random
print("HANGMAN")
wordlist = ['python', 'java', 'javascript', 'php']
a = random.choice(wordlist)
guesses = ''
attempts = 8
splitted_word = list(a)

while attempts > 0:
    missed = 0
    for letter in a:
        if letter in guesses:
            print (letter,end=' ')
        else:
            print ('_',end=' ')
            missed = missed + 1
    if missed == 0:
            print ('You win!')
            break

    guess = input('Input a letter: ')

    if guess not in a:
        if guess in guesses:
            print('No improvements')
        else:
            guesses += guess
            attempts = attempts - 1
            print("That letter doesn't appear in the word" )
    else:
        if guess in guesses:
            print('No improvements')
        else:
            guesses += guess

    
      




