# # Write a program that takes a string as input and prints the number of characters in the string.

# string1 = input("Enter the String: ")

# num = len(string1)
# print(num)

# Implement a function that reverses a given string and returns the reversed version.

# def reverse_string(string):
#     return string[::-1]

# value = input("Enter the value: ")
# reverse_string = reverse_string(value)
# print("reverse value : ", reverse_string)


# Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string.


# def count_vowels(string):
#     vowels = 'aeiou'
#     count = 0

#     for char in string.lower():
#         if char in vowels:
#             count += 1

#     return count

# input = input("Enter the String: ")
# vowel_count = count_vowels(input)

# print("Vowels in Strings are : ",vowel_count)


# Create a program that checks if a given string is a palindrome (reads the same forwards and backwards)

# def palindrome_text(string):
#     string = string.lower()

#     return string == string[::-1]


# user_input = input("Enter text : ")
# if palindrome_text(user_input):
#     print("Its a palindrome text")
# else:
#     print("Its not palindrome text")

#Implement a function that takes a sentence as input and returns the sentence with the words reversed.

# def reversed_word(string):
#     return string[::-1]

# user_input = input("Enter the word : ")

# print(reversed_word(user_input))

# Write a program that takes a string as input and converts all lowercase characters to uppercase, and vice versa.

# def change_case(string):
#     case_changed = ""
#     for a in string:
#         if a.islower():
#             case_changed += a.upper()
#         else:
#             case_changed += a.lower() 

#     return case_changed

# user_input = input("Enter the string: ")
# print(change_case(user_input))

#Create a program that counts the occurrence of each character in a given string and displays the frequency.

# def charater_count(string):
#     char_count = {}

#     for char in string:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1

#     return char_count
    
# User_input = input("Enter String: ")
# new = charater_count(User_input)

# for char, count in new.items():
#     print(f"Character '{char}' occurs {count} times")

#Implement a function that takes a sentence as input and returns the longest word in the sentence.

# def long_word(string):
#     string = string.split(" ")
#     long = ""

#     for i in string:
#         if len(i) > len(long):
#             long = i
    

#     return long

# user_input = str(input("Enter the sentence: "))
# print(long_word(user_input))

# Write a program that takes a string as input and removes all the punctuation marks from the string.

def remove_punctuation(string):
    word = string.split()
    punc = '?!'

    for word in string:
        if word :
            word.remove()

    return word.join()

user_input = input("Enter the puntuation sentence: ")

print(remove_punctuation(user_input))