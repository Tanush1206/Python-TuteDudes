a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Addition
add = a + b

# Subtraction
sub = a - b

# Multiplication
multi = a * b

print("\nAddition:", add)
print("Subtraction:",sub)
print("Multiplication:",multi)

# Division
if b == 0:
    print("Division by zero is not allowed")
else:
    div = a / b
    print("Division:", div)