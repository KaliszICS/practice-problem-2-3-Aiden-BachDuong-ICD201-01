'''

    Lesson: Else If Assignment
    Author: Aiden
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024

'''

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word.endswith("ife"):
    print("-ives")
  elif word.endswith("ey"):
    print("-eys")
  elif word.endswith("y"):
    print("-ies")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num >= 1:
    print(f"{num} is positive")
  elif num <= -1:
    print(f"{num} is negative")
 

def q3():
  #Write Assignment code here
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  num3 = float(input("Input a number: "))
  if num1 + num2 <= num3:
    print("No Triangle")
  elif num1 == num2 == num3:
    print("Equilateral")
  elif num1 != num2 != num3:
    print("Scalene")
  else:
    print("Isosceles")

#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
'''