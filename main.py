#Function Return

def Plus2(a,b):
  result=a+b
  return result

def Minus2(a,b):
  result=a-b
  return result
  
def Multiply2(a,b):
  result=a*b
  return result

def Divide2(a,b):
  result=a/b
  return result

def Story(name, age):
  result = "My name is "+ name +" and I'm "+age +" years old."
  return result

#School
#input - grade / teacher_name
#return string - Im 5th grade and my teacher is *****

def school(grade, teacherName):
  result = "I am grade " + grade + " and my teacher's name is " + teacherName
  return result

mygrade = "5th"
myteacherName = "John"
myschool = school(mygrade, myteacherName)
print(myschool)


a = 9
b = 3

c = Plus2(a,b)
d = Minus2(a,b)
e = Multiply2(a,b)
f = Divide2(a,b)
print (c)
print (d)
print (e)
print (f)

print("PLUS is "+str(c) + " and MINUS is " + str(d))


myName = "SONG"
myAge = "20"

myStory = Story(myName, myAge)
#print(myStory)
print("MY STORY RESULT: " + myStory)
print("MY STORY IS PERFECT!!! : " + myStory)



'''
def PLUS(a , b):
  c = a+b
  print("plus is "+str(c))

def Minus(a, b):
  c = a-b
  print("minus is "+str(c))
  
def Multiply(a, b):
  c = a*b
  print("product is "+str(c))

def Divide(a, b):
  c = a/b
  print("quotient is "+str(c))

def POW (a,b):
  c = pow(a, b)
  print("square is "+str(c))

condition = True

while(condition == True):
  print("---------------------------[Calculator]-------------------------")
  print("Calculator + - * / ^")
  number1=int(input(" number 1:"))
  number2=int(input(" number 2:"))
  operator=input(" operator? (+ - * / ^):")
  
  if (operator=="+") :
    PLUS (number1,number2)
  elif(operator=="-") :
    Minus (number1,number2)
  elif(operator=="*") :
    Multiply (number1, number2)
  elif(operator=="/") :
    if(number2==0) :
      print("anwser is infinity")
    else: 
      Divide (number1, number2)
  elif(operator=="^") :
    POW (number1, number2)
  else:
    print("[ERROR] Not an operator. Try again!!")

  print("----------------------------------------------------------------")
  user_answer = input("Press [N] to quit, Any key to continue.")
  if ( user_answer=="N" or  user_answer=="n"):
    condition=False
  else:
    condition=True


#Make Calculator with Function
'''