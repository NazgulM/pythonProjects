# Repeat one function in another function
#factorial is 5*4*3*2*1

def factorial(n):
    factNum = 1
    for i in range (1, n+1):
        factNum *= i
    return factNum


def recursion_factorial(n):
    if n == 1:
        return n
    return n * recursion_factorial(n-1)


def findEvenNumber(n):
    if n%2 == 0:
        return "Even Number"
    else:
        return "Odd number"
    

def findEvenNumber2(n):
    if n <2: 
        return n %2 == 0
    else:
        return findEvenNumber2(n-2)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Fibonacchi  - a set of integers (the Fibonacci numbers) that starts with a zero, 
# followed by a one, then by another one, and then by a series of steadily increasing numbers.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.

if __name__=="__main__":   
    # print(factorial(5))
    # print(recursion_factorial(5))
    # print(findEvenNumber(15))
    n = int(input("Number: "))
    # if (findEvenNumber2(n) == True):
    #     print("Even Number")
    # else:
    #     print("Odd Number")
    print("Fibonacci following")
    for i in range(n):
        print(fibonacci(i), end=' ' )
