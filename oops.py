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

# print(a.name)
# print(a.age)

# a.name = "Abhi"
# print(a.name)

# a.age = 18
# print(a.age)