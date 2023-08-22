# print("Hello World!!!")

# -----------------------------------------Python Input---------------------------------------------
# name = input("what is your name?")
# print(name)
# age = input("tell me your age")
# print(age)

# -----------------------------------------Python addition---------------------------------------------

# first_num = input("Tell me the First Number: ")
# second_num = input("tell me the second number: ")
# sum = int(first_num) + int(second_num)
# print("The sum of two number is: " + str(sum))

# -----------------------------------------Python inbuilt functions---------------------------------------------


# name = " Aniket Shrivastav"
# print(name.find('An'))
#
# print(name.replace(' ','King'))
#
# print('V' in name)
# print('Aniket' in name)


# -----------------------------------------Arithmetic Operators---------------------------------------------


# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5//2)
# print(5%2)
# print(5**2)
# i = 4
# i+=2
# print(i)
# i-=3
# print(i)
# i*=4
# print(i)

# -----------------------------------------Comparison Operators---------------------------------------------

# print(3>2)
# print(3==2)
# print(3>=2)
# print(2==2)
# print(3!=4)

# -----------------------------------------logical Operators---------------------------------------------

# print(2>3 or 1<2)
# print(2==3 and 3>2)
# print(3==3 and 2>1)
# print(not 2==3)


# -----------------------------------------IF / ELSE---------------------------------------------

# age = int(input())
# if(age>21):
#     print("You are an Adult")
# elif(age>17 and age<22):
#     print("You are a College undergrad")
# elif(age<18 and age>14):
#     print("You are a JEE/NEET aspirant")
# else:
#     print("You are a Noob!!!")

# -----------------------------------------Arithmetic Calculator---------------------------------------------


# a = (input())
# b = (input())
#
# operator = input()
#
# if(operator == '+'):
#     print(a+b)
# elif(operator == '-'):
#     print(a-b)
# elif(operator == '*'):
#     print(a*b)
# elif(operator == '/'):
#     print(a/b)
# elif(operator == '**'):
#     print(a**b)
# elif(operator == '//'):
#     print(a//b)
# else:
#     print(a%b)


# -----------------------------------------loops---------------------------------------------


# range(5) # 0,1,2,3,4
#
# i = 2
#
# while(i<7):
#     print(i)
#     i = i + 1
#
# i = 1
# while(i<6):
#     print(i * '*')
#     i = i+1
#
# for i in range(2,10):
#     print(i)
#     i+=1


# -----------------------------------------Lists---------------------------------------------

# marks = [10,20,30,45,321.33,12,"King Aniket",95]
#
# print(marks)
# print(marks[3])
# print(marks[-4])
# print(marks[2:6]) # not included 6
# print(marks[-1:2]) #not possible in reverse
#
#
# marks.append("King of IIIT Nagpur")
# print(marks)
# marks.insert(6,"THE BEST IN THE WORLD")
# print(marks)
#
# print('King' in marks)
# print(321.33 in marks)
#
# print(len(marks))
#
# marks.clear() # will clear all elements from list


# -----------------------------------------Breaks and Continue---------------------------------------------

# students = ["Aniket","Mansi","Mrunal","Sakshi","Vanshika","Radha","Anjali","Srishti","Arya"]
#
# for i in students:
#
#     if i =="Anjali":
#         continue
#     elif i =="Mansi":
#         print("Beautiful")
#     elif i == "Mrunal":
#         print("Old Story")
#     elif i == "Radha":
#         print("Most Desirable One")
#     elif i == "Arya":
#         break
#     else:
#         print("OkOkOk")

#they are mutable



# -----------------------------------------Tuples---------------------------------------------

#Tuples are immutable


# marks = (22,34,55,99,56,33,12,99,99,55,55,555,55,12)

# person = "aniket", "radha", "mansi", "mrunal"
#so this is a by default tuple
#
# print(marks.count(99))
# print(marks.count(55))
# print(marks.count(556))
# print(marks.index(55)) #starting index


# -----------------------------------------Sets---------------------------------------------

# #for unique elements
#
# marks = {22,3,11,22,11,44}
# print(marks)

# -----------------------------------------Dictonary---------------------------------------------


# key value pair data storage

# marks = {
#     "name" : "Aniket",
#     "roll" : 34,
#     "chemistry" : 45,
#     "maths" : 46
#
# }
#
# print(marks)
#
# marks["roll"] = 23
#
# print(marks)


# -----------------------------------------Functions---------------------------------------------

# In-Built Functions
# Module Functions
# User Defined Functions

from math import sqrt

print(sqrt(9))
print(sqrt(34))

def print_sum(a=4,b=5):
    return a+b

print(print_sum())
print(print_sum(2,3))
print(print_sum(2))


# -----------------------------------------End of Basics of Python---------------------------------------------
