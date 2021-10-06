print("HANGMAN")
list = ['python', 'java', 'javascript', 'php']
import random
(random.choice(list))
a = input(str("Guess the word:"))
if a==(random.choice(list)):
    print("You survived!")
else:
    print("You lost!")
