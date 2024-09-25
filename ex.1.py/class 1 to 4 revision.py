print("exercise 1:")
first_name = "Kenil"  
last_name = "Jodhani"    

print(f"Hello, {first_name}! Welcome to the program.")
print("\n\n")


print("exercise 2:")

d1 = "Milk"
d2 = "Water"

print(f"Original values: Drink 1 = {d1}, Drink 2 = {d2}")
drink1, drink2 = d2, d1

print(f"Swapped values: Drink 1 = {drink1}, Drink 2 = {drink2}")
print("\n\n")



print("exercise 3:")

last_name = "jodhani"
first_name = "kenil"

full_name = last_name + first_name

print(f"{full_name}")


print("excerise 4:")

num1 = 10
num2 = 5
print(f"addition: {num1} + {num2} = {num1 + num2}")


print("exercise 5:")
numlist = [1, 2, 3, 4, 5]

print(f"first element: {numlist[0]}")
print(f"last element: {numlist[-1]}")

print("execrise 6:")
i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(1, 11):
    print(i)


print("exercise 7:")

number = 12

if number >= 10:
    print(f"The {number} is greater than or equal to 10.")

else:
    print(f"The {number} is less than or equal to 10.")
print("\n\n")    



print("exercise 8:")


def greet(name):
     print(f"Hello, {name}! Welcome to the program.")

greet("Kenil")








print("exercise 9:")

my_dict = {
    "name": "Kenil",
    "age": 24,
    "city": "Dallas"
}
print("The value of the key 'age' is:", my_dict["age"])
print("\n\n")


print("excricse 10:")

counter = 1

# Start the while loop
while counter <= 5:
    print(counter)
    counter += 1 
print("\n\n")


print("exercise 11:")

person = {
    "name": "Kenil",
    "age": 24,
    "city": "Dallas"
}
print("The value of the key 'name ' is:", person["name"])
print("\n\n")

print("exercise 12:")

def calculate(num1, num2, operation="add"):
    if operation == "substact":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return num1 + num2

print("Addition :", calculate(10, 5))              
print("Subtraction:", calculate(10, 5, "subtract"))         
print("Multiplication:", calculate(10, 5, "multiply"))     
print("Division:", calculate(10, 5, "divide"))             
print("Invalid operation:", calculate(10, 5, "modulus"))
print("\n\n")







print("execrise 13:")
yearlist = [1990, 1991, 1992, 1993, 1994, 1995]

agelist = []
currentyear = 2024

for year in yearlist:
    age = currentyear - year
    agelist.append(age)

    print(f"List of ages: {age}")
