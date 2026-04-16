firstDigit  = input("Enter first digit :")
operation = input(f"select operation \n1.+ \n2.- \n3.%  \n4./ \n5.square root \n6.x \n")

def sqrt(firstDigit):
   ans = firstDigit * firstDigit
   print(ans)


if int(operation) == 5:
   sqrt(int(firstDigit))
else :
   lastDigit = input("select last input :")


def add(firstDigit,lastDigit):
   ans=int(firstDigit) + int(lastDigit)
   print(ans)

if int(operation) == 1 :
   add(int(firstDigit),int(lastDigit))

def differance(firstDigit,lastDigit):
   ans=int(firstDigit) - int(lastDigit)
   print(ans)

if int(operation) == 2 :
   differance(int(firstDigit),int(lastDigit))

def modulus(firstDigit,lastDigit):
   ans=float(firstDigit) % int(lastDigit)
   print(ans)

if int(operation) == 3 :
    modulus(int(firstDigit),int(lastDigit)) 

def division(firstDigit,lastDigit):
   ans=int(firstDigit) / float(lastDigit)
   print(ans) 

if int(operation) == 4:
   division(int(firstDigit),int(lastDigit))

def multiply(firstDigit,lastDigit):
   ans = int(firstDigit) * int(lastDigit)
   print(ans)

if int(operation) == 6 :
   multiply(firstDigit,lastDigit)