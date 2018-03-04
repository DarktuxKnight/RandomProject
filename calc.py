#argv = argv[1:]  # Reduce the argument list by copying it starting from index 1


import random
import string

def calcs(args):

    a=args[0]
    b=args[1]
    operation=args[2]

    if operation == '+':
        print(a,operation,b,'=',a+b)
    elif operation == '-':
        print(a,operation,b,'=',a-b)
    elif operation == '*':
        print(a,operation,b,'=',a*b)
    elif operation == '/':
        print(a,operation,b,'=',a/b)
    elif operation == '%':
        print(a, operation, b,'=',a%b)
    elif operation == '//':
        print(a,operation,b,'=',a//b)
    elif operation == '**':
        print(a,operation,b,'=',a**b)

while True:
    opplist = ['+','-','*','/','%','//','**']
    operation = input(''' 
    Addition : '+'
    Subration : '-'
    Multiplecation : '*'
    Divison : '/'
    Modulus : '%'
    Quotient : '//'
    To the Power of : '**'
    Please do select one of the below operations: ''')
    if operation in opplist:
        break
    else:
        print("Invalid Input, please try again!")

a = int(input("Enter 1st digit: "))
b = int(input("Enter 2nd digit: "))

inputarray = [a,b,operation]
#print(inputarray)
calcs(inputarray)