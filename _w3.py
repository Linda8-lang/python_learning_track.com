x="Hello"[0]
print(x)# Type of variable #print(type(x))
def check_temperature ():
    print(''' It is cold so do the following:
    Carry an umberallla
    Wear warm clothes.
    Wear gloves.
    Drink plenty of warm water.
    ''')

check_temperature()
def my_details (fname, lname, age):
    print(fname + lname + str(age))
my_details("Linda ","Aluso ", 31)

def my_country(country="Sweden"):#Default parameter value
    print("My country of origin is " + country)
my_country("Kenya")
my_country("Norway")
my_country()
my_country("Estonia")

def my_function(food):#Passing list as an argument,example1
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
def subject_choice (subjects):#Passing list as an argument
  for items in subjects:
    print(items)
selection =["Mathematics", "Biology", "Physics", "Chemistry"]
subject_choice(selection)

#Recursion, a function calling itself
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(0)
 