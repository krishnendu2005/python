

# print(r"c:\desktop:\new.txt")
# print(r"c:\desktop:\ten.txt")
# #
# a=10
# b=a
# a=20
# print(a)
# print(b)
# name=input("what is you name ")
# age=input("what is your age")
# n2=(f"hi {name} you are {age} years old ")
# print(name)
# print(age)
# print(n2)
# #new 
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# print(a+b)
# #vote
# age=int(input("enter age:"))
# if age>18:
#     print("eligible")
# else:
#     print("not eligible")
    #marksheet
# num=int(input("enter a no:"))
# if num>=100 & num>=90:
#     print("grade A")
# elif num>=90 & num>=80:
#     print("grade B")
# elif num>=80 & num>=70:
#     print("grade C")
# else:
#     print("Fail")
    
#     #string
# str = input("Enter a string: ")


# lowercase_string = str.lower()

# print("String in lowercase:", lowercase_string)

#list
# fruits = ["apple", "banana", "cherry"]

# print("First fruit:", fruits[0])  
# print("Last fruit:", fruits[-1]) 

# fruits.append("date")
# print("List after adding a fruit:", fruits)

# #tuple
# abc = ("apple", "banana", "cherry")

# banana_count = abc.count("banana")
# print("Number of 'banana' in the tuple:", banana_count)

 #lsit & set 
 
# my_list = [1, 2, 2, 3, 4, 4, 5]  

# print("List:", my_list)  
# my_set = {1, 2, 2, 3, 4, 4, 5}   
  
# print("Set:", my_set)    

# #subset & superset
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# print("Is A a subset of B?", A.issubset(B))  

# print("Is B a superset of A?", B.issuperset(A))  

# C = {1, 6}
# print("Is C a subset of B?", C.issubset(B))  

# print("Is B a superset of C?", B.issuperset(C))  


# #difference & symmetric diff

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print("A & B:", A.difference(B))  
# print("B & A:", B.difference(A))  

# print("A & B:", A.symmetric_difference(B))  


#loop

# i = 5
# while i > 0:
#     print(i)
#     i -= 1
#nested loop


for i in range(1, 6):  
    
    for j in range(1, 6):  
        print(i * j, end="\t")  
    print()  
