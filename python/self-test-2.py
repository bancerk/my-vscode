#!/usr/bin/python3

# simple calculator

num_1 = input("Please enter your first number:")

num_1 = float(num_1)

num_2 = input("Please enter your second number:")

num_2 = float(num_2)

my_op = input("Please enter your desired operation:")

if(my_op == "+"):
    print(num_1 + num_2)
elif(my_op == "-"):
    print(num_1 - num_2)
elif(my_op == "*"):
    print(num_1 * num_2)
elif(my_op == "/"):
    print(num_1 / num_2)
elif(my_op == "%"):
    print(num_1 % num_2)
else:
    print("Invalid operation") 