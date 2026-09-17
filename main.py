print("")
print("== using xor to detect signs ==")
print("")

num = 78
num1 = -4

print(f"first number: {num}\nsecond number: {num1}")
print("")

if (num < 0) ^ (num1 < 0):
    print(f"{num} and {num1} have different signs")
else:
    print(f"{num} and {num1} have the same signs")