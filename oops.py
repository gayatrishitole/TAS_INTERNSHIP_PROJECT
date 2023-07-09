# Class , method and object 

# class car:
#     name = 'Harrier'
#     Company = 'TATA'
#     Prize = 2000000
#     def info(self):
#         print(f"{self.name} is car of {self.Company} company and prize is {self.Prize}")

# a = car()
# # print(a.name, a.Company)

# # b = car()
# # b.name = 'Thar'
# # b.Company = 'Mahindra'
# # print(b.info())

# print(a.info())


# class car:
#     def __init__(self, model, prize, company) :
#         self.model = model
#         self.prize = prize
#         self.comapany = company

#     def info(self):
#         print(f"{self.model} is car of {self.comapany} and prize is {self.prize}")


# a = car('Harrier', 2000000, 'TATA')
# print(a.info())

## Getters and Setters

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age
    
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     @age.setter
#     def age(self, new_age):
#         if new_age > 0:
#             self._age = new_age


        
# a = Person("Aditya", 21)

# # print(a.name)
# # print(a.age)

# a.name = "Abhi"
# print(a.name)

# a.age = 18
# print(a.age)

# Static Method

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# print(Math.add(7,9)) # so here no need of instance to called the method we can directly access it by class by using static method

# import os

# # os.rename("C:/Users/Hp/OneDrive/Documents/Productivity tool/python-practice/list.text", "C:/Users/Hp/OneDrive/Documents/Productivity tool/python-practice/new.txt")
# i = 1
# files = os.listdir("C:/Users/Hp/OneDrive/Documents/Productivity tool/python-practice/imagepng")
# for file in files:
#     if file.endswith(".png"):
#       print(file)
#       os.rename(f"C:/Users/Hp/OneDrive/Documents/Productivity tool/python-practice/imagepng/{file}", f"C:/Users/Hp/OneDrive/Documents/Productivity tool/python-practice/imagepng/{i}.png")
#       i = i + 1