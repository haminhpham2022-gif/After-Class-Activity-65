def multiply(a, b):
    return a << b

def divide(a,b):
    return a >> b

print("=== Calculator ===")
print("Do you want to do a) Multiplication or b) Division?")
x = str(input("a or b: "))

if x == "a":
    firstnum = int(input("Enter your number: "))
    secondnum = int(input("By which power do you want to multiply: "))
    print(multiply(firstnum, secondnum))
elif x == "b":
    firstnum = int(input("Enter your number: "))
    secondnum = int(input("By which power do you want to divide: "))
    print(divide(firstnum, secondnum))
else:
    print("invalid input")