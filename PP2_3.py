

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word [-1:] == "y":
    print("-ies")
  elif word [-2:] == "ey":
    print("-eys")
  elif word [-3:] == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num >= 1:
    print(f"{num} is positive")
  elif num <= -1:
    print(f"{num} is negative")
  else:
    print()


#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
'''