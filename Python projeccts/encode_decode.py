import string
import random

def encode(word):
    if len(word) >= 3:
        word = word[1:] + word[0]
        random_char = "".join(random.choice(string.ascii_lowercase ) for _ in range(3))   
        word = random_char + word + random_char
    else:
        word = word[::-1]
    return word

def decode(word):
    if len(word) >= 3:
        random_char = word[:3]
        word = word[3:-3]
        word = word[-1] + word[:-1]
    else: 
        word = word[::-1]
    return word


def encrypt_decrypt(word):

    test = int(input("Do you want to encode or decode (1/0): "))
    if test == 1:
        return encode(word)
    
    elif test == 0:
        return decode(word)
    
    else:
        print("Invalid choice!")

word = input("Enter something: ")
x = encrypt_decrypt(word)
print(x)
