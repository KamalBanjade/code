# print("hey i am kamal banjade and i have started my python journey from today")
# #this is the comment line
# """kamal
# banjade
# multiline 
# comment
# """
# # control / is used to comment out
# # to make something in double quite we must use escape statement \" infront and back of the word which we wanna make double quote and similarly in single quote too
# print(" hey this is \"kamal banjade\" and i wanna put kamal banjade in double quote")
# print ("hey i am\' kamal banjade and i wanna put a single quote after am")
# # to use seperator between diff num and letters we have to use sep function and end is used to add something in another print line
# print("hey", 4,5, sep="^", end="kamal")
# print("banjade")
# a = 1
# b = True
# c = "Harry"
# d = None
# # to find the date type code is such as 
# print(a)
# print("the data type of a is",type(a))
# print("the data type of a is",type(a))
# print("the data type of c is",type(c))\

#  # operators
# print(5+6)
# print(5-6)
# print(5*6)
# print(5/6)
# print(5//6) #mode
# print(5%6) #mode
# print(5**3)#exponential

# # alt+shift+downarrow to duplicate line 
# """

# #this is print for two different print statements
# print("i am kamal" ,end=".")
# print("i am doing coding")
# #this is print for single line print statements here "," gives space
# print("i am kamal","i am doing coding",end="_")

# #\n is a line breaker and \t is a tab
# print("c:\n \"coding journey")#while giving location \ is must
# print("kamal is \n a good boy \t")
# #variable
# var1 ="kamal"
# print(type("var1"))

# var2="bimla"
# print(type(var2))
# print(var1+var2)

# var3="20"
# var4="30"
# #if we put"" insibe the print statement it will print exactly what is there and if we don't put it will print the conditions inside it
# #we can use int after print statement to calculate integer if it is string
# #similarly we have functions like str(), float()etc
# print(int(var3)+int(var4))
# #to print many times we have to do just multiply the numbwer we want suck like:
# print(10*"kamal banjade\n")
# #to multiply it must be in string
# var5="10"
# var6="30"
# print(10* str(int(var5+var6)))
# #intnum is variable here
# """
# """print("enter a number")
# intnum = input()
# print("you entered",int(intnum)+10)"""

# #sum of two numbers
# """
# print("enter a first number")
# n1 = input()
# print("enter a second number")
# n2 = input()
# sum = int(n1)+int(n2)
# print("the sum is",sum)
# """
# #difference of two number
# """
# print("enter the first number")
# n3 = input()
# print("enter the second number")
# n4 = input()
# difference = int(n3)-int(n4)
# print("the difference is",difference)
# """
# #product of two numbers
# """
# print("enter the first number")
# n5 = input()
# print("enter the second number")
# n6 = input()
# product = int(n5)*int(n6)
# print("the product is",product)
# """

# mystr = "kamal is a good person"
# print(mystr)

# '''
# print("enter the first number")
# num1 = input()
# print("enter a second number")
# num2 = input()
# sum = int(num1)+int(num2)
# print("the sum of two numbers is",sum)
# diff = int(num1)-int(num2)
# print("the diff of two numbers is",diff)
# prod = int(num1)*int(num2)
# print("the product  of two numbers is",prod)
# div= int(num1)/int(num2)
# print("the division of two numbers is",div)
# float = int(num1)//int(num2)
# print("the float of two numbers is",float)
# '''
# # to print in multiline we can use single triple quote or double triple quote
# # for an example
# k="""
# hi i am kamal banjade
# i am from kathmandu 

# """
# print(k)

# Name ="kamal"
# # print(Name[0])
# # print(Name[1])
# for character in Name:
#     print(character)

# # TO FIND THE LENGTH OF STRING WE USE THE LEN FUNCTION
# Name= "kamal"
# print(len(Name))

# fruit=("apple")
# len1 =len("apple")
# print("mango is a" ,len1 ," letter fruit")
# # string slicing
# print(fruit[0:4])#starting with 0 but don't end in 4
# print(fruit[:4])#by default zero
# print(fruit[2:3])
# print(fruit[0:-1])#length of fruit is 5 so 5-1 =4
# print(fruit[-3:-2])#here 5-3=2,5-2=3 so python will compile it as 2:3
# nm="harry"
# print(nm[-4:-2])

# # STRINGS ARE InMUTABLE
# # TO MAKE EVERYTHING IN UPPPER case
# a="kamal"
# print(len(a))
# print(a.upper())
# # IN EVERY CASE NEW STRING IS CREATED COZ STRINGS ARE UNCHANGELE
# # SIMILARLY IN LOWER CASE 
# a="KAMAL"
# print(a.lower())
# # to remove the sign from string rstrip is used
# # it only removes last sign not front one
# b="kamal!!!!!"
# print (b.upper())
# print (b.rstrip("!"))
# print(b.replace("kamal","banjade"))
# #to split 
# c="!!!! kamal !!!!"
# print(c.split(" "))
# #to make only first letter capital
# Name= ("sumitra")
# print(Name.capitalize())
# #to align something in centre
# E="hi i am kamal banjade !!!"
# print(len(E))
# print(len(E.center(50)))
# print(E.endswith("!!!"))
# f=("Khagishwor")
# print(f.isalnum ())
# print(E.find("kamal"))
# #to check whether the given string is lower case or not
# g="kamal"
# print(g.islower())
# h="kamal"
# print(h.isprintable())
# i="Kamal"
# print(i.istitle())#to check whether the first letter is capital or not
# j= "kamal"
# print(j.isupper())
# k="python is a programming launguage"
# print(k.swapcase())
# l="i am learning python ."
# print(l.startswith(i))

# if else 
# 2

#if elif else
# b= int(input("enter a number : "))
# if b>0:
#     print("the number is positive")
# elif b<0:
#     print("the number is negative")
# else:
#     print("the number is zero")

# #nested if
# c=int(input("enter a number"))
# if c>10:
#     print("the number is more than 10")
# elif c<10:
#     if c<=20:
#         print("the number is between 1- 20")
#     elif c<=40:
#         print("the number is between 1-40")
#     else:
#         print ("he is average") 

# elif c==5:
# #     print("he is failed")  

# d=int(input("enter a number : ")) 
# if d<0:
#     print("the number is negative")
# elif d>0:
#     if d<= 10:
#         print("the number lies between 1- 10")
#     elif d<= 20:
#         print("the number lies between 1 - 20")
#     else:
# #         print("the number is greater than 20")
# # else:
# #     print("the number is zero")  
 
# e="hi i am kamal banjade and i am a good person"
# print("10*e", end="\n")

# statement = "I am a good person."

# for i in range(10):
#     print(statement)

# print(10*"hi i am kamal banjade and i am a good person \n")

# k=int(input("enter a time"))
# if k < 12 :
#     print("good morning, have a good day")
# elif k>12:
#     if k==12:
#         print("hey it's noon")
#     elif k<12 >18:
#         print("hey good afternoon")
#     elif k<18>22:
#         print("good evening")
#     elif k<22>24:
#         print("good night")
# else:
#     print("it's going to be morning")

# import time
# timestamp = time.strptime ("%H:%M:%S")
# print(timestamp)
# timestamp = time.strptime("%H")
# print(timestamp)
# timestamp = time. strptime("%M")
# print(timestamp)
# timestamp = time. strptime("%S")
# print(timestamp)

x = int(input("enter a value of x : "))
match x:
    case 0:
        print("case is zero")
    case 4:
        print("case is four")
    case _ :
        print("x")



# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     # case _ if x!=90:
#     #     print(x, "is not 90")
#     # case _ if x!=80:
#     #     print(x, "is not 80")
#     case _:
#         print(x)
