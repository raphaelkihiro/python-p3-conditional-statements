#!/usr/bin/env python3

def admin_login(username, password):

     # your code here
        if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
   
    pass

def hows_the_weather(temperature):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def fizzbuzz(num):
    # your code here
        if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

    pass

def calculator(operation, num1, num2):
    # your code here
     if operation == "+":
        print (num1 + num2)
    elif operation == "-":
        print (num1 - num2)
    elif operation == "*":
        print (num1 * num2)
    elif operation == "/":
     print (num1 / num2)
    else:
        print("Invalid operation!")
        return None
    pass
