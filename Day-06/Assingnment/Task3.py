## Task 3: Logical Operators

print("Logical Operators in Python")
print ( " enter 4 numbers: " )
a = float(input())
b = float(input())
c = float(input())
d = float(input())

if a > b and c > d:
    print(f"{a} is greater than {b} AND {c} is greater than {d}")
if a < b or c < d:
    print(f"{a} is less than {b} OR {c} is less than {d}")
    