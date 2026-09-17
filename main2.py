a,b = 5,9
print(f"a = {a}, b = {b}")

a ^= b
b ^= a
a ^= b

print(f"After Swapping \na = {a}\nb = {b}")