#Question 1:

def reverseString(s,i):
  new_string = s[ : :-1] * i
  print(new_string) 

reverseString ("hello" , 3)

#Question 2:

def rearrangeString(s):
    upper_case_letters = ""
    lower_case_letters = ""

    for char in s:
      if char.isupper():
        upper_case_letters += char
      else:
        lower_case_letters += char

    print(upper_case_letters + lower_case_letters)
  
  
  
rearrangeString("HEllo World")

#Question 3:

def func1(string1, string2):
  count1 = {}
  for char in string1:
    if char in count1:
      count1[char] += 1
    else:
      count1[char] = 1

  for char in string2:
    if char not in count1 or count1[char] == 0:
      return False

    count1[char] -= 1

  return True


s1 = input("enter string 1: ")
s2 = input("enter string 2: ")
print(func1(s1,s2))
    


#Question 4:

def max(list1):
  max_value = list1[0]
  max_index = 0
  for i in range(1,len(list1)):
    if list1[i] > max_value:
      max_value = list1[i]
      max_index = i
  return max_value , max_index
  
max_value, max_index = max([1,2,3,4,5])

print ("the highest value in the list is" , max_value ,"of index " , max_index)

def min(list1):
  min_value = list1[0]
  min_index = 0
  for i in range(1,len(list1)):
    if list1[i] < min_value:
      min_value = list1[i]
      min_index = i
  return min_value , min_index

min_value, min_index = min([1,2,3,4,5])

print ("the lowest value in the list is" , min_value ,"of index " , min_index)



#Question 5:

def digitSum(n):
  if n < 10:
    return n
  else:
    return n % 10 + digitSum(n // 10)

#Question 6:

def func3(s):
    if len(s) <= 1:
      return s
    elif s[0] == s[1]:
      return func3(s[1:])
    else:
      return s[0] + func3(s[1:])


print(func3('hhellooo wwwwwoorldddd'))

