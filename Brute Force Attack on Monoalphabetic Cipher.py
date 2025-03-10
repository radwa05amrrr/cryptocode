from operator import index
from random import shuffle
def monoalphabetic_brute_force (text,attempts):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(attempts):
        shuffled = letters[:]
        shuffle(shuffled)
        plain_text = ""

        for char in text:
            if char in letters:
                location = letters.index(char)
                plain_text += shuffled[location]
            else:
                plain_text +=char

        print(f"Attempt {i + 1}: {plain_text}")

text = input("Enter your cipher text: ")
attempts = int(input("Enter number of attempts: "))

monoalphabetic_brute_force(text,attempts)
