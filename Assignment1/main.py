#Question 1:

print("10*(90+2)-5= " ,  10*(90+2)-5)
print("10*90+2-5= "  , 10*90+2-5)
print("10*90+(2-5)= " , 10*90+(2-5))
print("10.0*(90+2)-5= " , 10.0*(90+2)-5)
print("120/(20+40)-(6-2)/4= " , 120/(20+40)-(6-2)/4)
print("5.0/2 = " , 5.0/2)
print("5/2 = " , 5/2)
print("5.0/2.0 = " , 5.0/2.0)
print("5/2.0 = " , 5/2.0)
print("678%3*(8-(9/4)) = " , 678%3*(8-(9/4) ))

#Question 2:
ID = input("What is your ID?:")
name = input("What is your name?:")
date_of_birth = input("What is your DOB?:")
address = input("What is your address?:")

if date_of_birth.__contains__("/"):
    day, month, year = date_of_birth.split("/")
else:
    day, month, year = date_of_birth.split("-")

formatted_date_of_birth = f"{day}/{month}/{year}"

print("Your profile - ID: 0" +  ID.replace(" ","") + ", name: " + name.upper().replace(" ","") +", DOB: "
        + formatted_date_of_birth.replace(" ","") + " ,Address: " + address.strip().lower().replace(" ",""))

#Question 3:

number = input("Please insert a number : ")

print(len(number))

#Question 4:

grade = int(input("Please enter your grade: "))

if grade >= 97:
    print(grade , "is equivalent to A+")
elif grade >= 93:
    print(grade, "is equivalent to A")
elif grade >= 90:
    print(grade, "is equivalent to A-")
elif grade >= 87:
    print(grade, "is equivalent to B+")
elif grade >= 83:
    print(grade, "is equivalent to B")
elif grade >= 80:
    print(grade, "is equivalent to B-")
elif grade >= 77:
    print(grade, "is equivalent to C+")
elif grade >= 73:
    print(grade, "is equivalent to C")
elif grade >= 70:
    print(grade, "is equivalent to C-")
elif grade >= 67:
    print(grade, "is equivalent to D+")
elif grade >= 63:
    print(grade, "is equivalent to D")
elif grade >= 60:
    print(grade, "is equivalent to D-")
else:
    print(grade, "is equivalent to F")



#Question 5:

n = input("Please insert an integer number: ")

while not n.isnumeric():
    n = input("Please insert an integer number: ")

n = int(n)
for i in range(0, n + 1):
    print("*" * i)
for j in range(n - 1, 0, -1):
    print("*" * j)


# before adding extra layer of validation this was my initial solution
# n= eval((input("Please insert a number: ")))
#
# for i in range(0, n+1):
#     print("*"*i)
# for j in range (n-1 ,0 , -1 ):
#     print("*"*j)

#Question 6:

n1 = int(input("Please insert a first number: "))
n2 = int(input("Please insert a second number: "))

while n2 < n1:
    print("the second number should be bigger than the first number!")
    n2=int(input("Please insert a second number: "))

for i in range(n1 , n2 + 1):
    if i % 2 == 0:
        print(i)












