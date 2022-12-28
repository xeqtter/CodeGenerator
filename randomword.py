# This is my first professional project that will be used for work purpose!
import random

WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
"""
    Welcome to WORD JUMBLE!!!

    Unscramble the leters to make a word.
    (press the enter key at prompt to quit)
    """
    )
print("The jumble is:", jumble)
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it, you guessed it!\n")
print("Thanks for playing")

input("\n\nPress the enter key to exit")

###############################################################################

from urllib.request import Request, urlopen
url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
print(webpage)
###################################################################################


from urllib.request import Request, urlopen
import random


url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
first500 = webpage[:500].split("\n")
random.shuffle(first500)
print(first500)
##############################################################################################

import random
import string

letters = string.ascii_letters
x = "".join(random.sample(letters,5))
 print(x)
############################################################################################