# pass statement is a null operation,
# and is used for when the statement is required syntactically
# but you want to keep the loop running and 
# you do not wish to execute any command of code

for x in "Edureka!":
    if x == "r":
        pass
        print("pass executed")
    print(x)
print("loop has ended")