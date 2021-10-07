import random
print("HANGMAN")
wordlist = ['python', 'java', 'javascript', 'php']
a = random.choice(wordlist)
guesses = ' '
attempts = 5

while attempts > 0:
     missed = 0
     for letter in a:
         if letter in guesses:
             print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed= missed + 1

     print

     if missed == 0:
         print ('You win!')
         break

     guess = input('Input a letter: ')
     guesses += guess

     if guess not in a:
         attempts = attempts - 1
         print ("That letter doesn't appear in the word")



