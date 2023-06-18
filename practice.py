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

# def remove_punctuation(string):
#     word = string.split()
#     punc = '?!'

#     for word in string:
#         if word :
#             word.remove()

#     return word.join()

# user_input = input("Enter the puntuation sentence: ")

# print(remove_punctuation(user_input))

## If else 

# Write a program that checks if a number is positive, negative, or zero. Take the number as input from the user.

# def num_check(num):
#     if num < 0 :
#         return "Negative"
#     elif num > 0 :
#         return "Positive"
#     else:
#         return "Zero"
    
# ip = int(input("Enter the Number: "))
# print(num_check(ip))

# Write a program that determines whether a year entered by the user is a leap year or not. A leap year is divisible by 4, but not divisible by 100, except if it is divisible by 400.

# def leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return "Leap Year"
    
#     else:
#         return "Not a Leap year"
    
# ip = int(input("Enter the Year: "))
# print(leap_year(ip))

# Write a program that checks if a given number is even or odd. Take the number as input from the user.

# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# ip = int(input("Enter the Number: "))
# print(even_odd(ip))

# Write a program that compares two numbers entered by the user and prints the larger number.

# def large_num(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
    
# io = int(input("Enter the number A: "))
# ip = int(input("Enter the number B: "))
# large_number = large_num(io,ip)

# print("Larger Number is :  ",large_number)

# Write a program that determines the grade of a student based on their score. The program should take the score as input and print the corresponding grade according to the following conditions:

# Score greater than or equal to 90: Grade A
# Score between 80 and 89: Grade B
# Score between 70 and 79: Grade C
# Score between 60 and 69: Grade D
# Score less than 60: Grade F

# def score(grade):
#     if grade >=90:
#         return "Grade A "
#     elif grade >= 80:
#         return "Grade B"
#     elif grade >= 70:
#         return "Grade C"
#     elif grade >= 60 :
#         return "Grade D"
#     else:
#         return "Grade F"
    
# ip = float(input("Enter the marks: "))
# grades = score(ip)
# print("The graden is : ",grades)

# Question: Create a program that takes a day of the week as input and prints a corresponding message based on the following conditions:

# If the day is "Monday" or "Tuesday", print "Work mode on!"
# If the day is "Wednesday", print "Halfway through the week!"
# If the day is "Thursday" or "Friday", print "Weekend is near!"
# For any other day, print "Enjoy your day!"


# def chech_the_day(day):
#   match day:
#     case "monday"  | "tuesday" :
#         print("Work mode on!")
#     case "wednesday":
#         print("Halfway through the week!")
#     case "thursday" | "friday" :
#         print("Weekend is near!")
#     case _:
#          print("Enjoy your day!")

# input_day = input("Enter the day name: ")
# chech_the_day(input_day)

## For loop

# for i in range(7):
#     print(i)

# for i in range(10,20,2):
#     print(i)

# name = "aditya"
# for i in name:
#     print(i, end =" ,")

# Question 1:
# Write a program that prints the multiplication table of a given number. The table should be printed from 1 to 10.

# user_input = int(input("Enter the number: "))

# for i in range(1,11):
#     print(i * user_input)

# Question 2:
# Write a program that counts the number of vowels in a given string. Consider both uppercase and lowercase vowels.

# def vowels(string):
#     char_count = {}

#     for char in string:
#         if char in char_count:
#             char_count[char]+= 1
#         else:
#             char_count[char] = 1
    
#     return char_count

# user_input = input("Enter the string: ")
# new = vowels(user_input)

# for char, count in new.items():
#     print(f"Vowel {char} is repeated {count} times")

# Write a program that prints the Fibonacci series up to a specified number of terms. 
# The Fibonacci series starts with 0 and 1, and each subsequent term is the sum of the previous two terms.

# user_input = int(input("Enter the number: "))

# a, b = 0,1
# fib_series = [a,b]
# for i in range (2,user_input):
#     c = a + b
#     fib_series.append(c)
#     a,b = b,c

# for num in fib_series:
#     print(num)

# Write a program that takes a list of numbers as input and finds the sum of all even numbers in the list.

# number = [1,23,34,56,34,2,1,3,65,78,9,23,24,46]
# sum = 0
# for i in number:
#     if i % 2 == 0 :
#       sum = i + sum
# print(sum)

# def sum_even_numbers(numbers):
#     sum_even = 0

#     for num in numbers:
#         if num % 2 == 0:
#             sum_even += num

#     return sum_even


# # Example usage
# user_input = input("Enter a list of numbers separated by spaces: ")
# numbers = [int(num) for num in user_input.split()]
# result = sum_even_numbers(numbers)
# print("Sum of even numbers:", result)

# Write a program that takes a list of words as input and prints the longest word in the list.

# def long_word(string):
#     longest_word = " "
#     for i in string:
#         if len(i) > len(longest_word):
#             longest_word = i
#     return longest_word
        
# user_input = input("Enter a list of strings separateed by spaces: ")
# list_size = [str(j) for j in user_input.split()]
# result = long_word(list_size)
# print("The longest word in list is : ",result)

# While loop

# Write a program that prints all the prime numbers between 1 and a given number.

user_input= int(input("Ente the number: "))
n = 2
i = []

while n < user_input :
    i.append(n)
    n+=1

for num in i :
    prime = True
    divisor = 2
    while divisor <= int(num**0.5):
        if num % divisor == 0:
            prime = False
            break
        divisor += 1

    if prime:
        print(num)

