import random
print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
b = (random.choice(words))
c = b[:3] + '-' * (len(b)-3)
splitted_words = list((random.choice(words)))
a = input(str("Guess the word" + " " + c + ":"))
if a==b:
    print("You survived!")
else:
    print("You lost!")
    print(c)

