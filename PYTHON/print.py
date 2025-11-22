# Exercise 3: Return multiple values from a function
# solution1
def caluculation(a,b):
    addition=a+b
    substration=a-b
    return addition,substration
res= caluculation(40,10)
print(res)

# solution2
def calculation(a,b):
    return a+b,a-b
add,sub=calculation(40,10)
print(add,",",sub)
    
# Exercise 4: Create a function with a default argument

def show_empoloyee(name,salary=9000):
    print("Name:",name,"\nSalary:",salary)
show_empoloyee("Ben",12000)
show_empoloyee("Jessa")


# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

print(list(range(4,30,2)))

even_num=[]

for num in range(4,31):
    if num%2==0:
        even_num.append(num)
    else:
        pass
    print(even_num)

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

x = [4, 6, 8, 24, 12, 2]
print(max(x))
var= "James Bond"
print(var[2::-1])

x = 36 / 4 * (3 +  2) * 4 + 2
print(x)


var = "James" * 2  * 3
print(var)
def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)