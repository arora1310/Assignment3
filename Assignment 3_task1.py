print("Welcome to factorial calculator")
a = int(input('Enter the number: '))

fact = 1


def factorial(num):
    global fact
    while num > 1:
        fact *= num
        num = num - 1
    return fact


factorial(a)
print(f"The Factorial of {a} is: {fact}")
