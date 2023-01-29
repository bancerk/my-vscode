# when "r" is encountered, the value is skipped,
# so the print statement for "r" is not executed,
# but continues for the rest of the statement
  

for x in "Edureka!":
    if x == "r":
        continue
    print(x)
print("loop has ended")