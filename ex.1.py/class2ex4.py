n = 10
def factorial(n):
    
    if n ==  0 or n == 1 :
        return 1

    else:     
        return n * factorial(n-1)

result = factorial(n)
print(f"factorial of the number is {result}.")
