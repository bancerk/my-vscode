#syntax
#if(test expression): 
    #statements when the condition is met
#elif(test expression):
    #statements when the elif condition is met
#else: 
    #final statements

x = 11
if x % 3 == 0:
    print("x is divisible by 3")
elif x % 5 == 0:
    print("x is divisible by 5")
else:
    print("x is not divisible by 3 or 5")