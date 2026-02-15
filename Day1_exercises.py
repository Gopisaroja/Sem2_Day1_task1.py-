n = int(input("Enter a number :"))
temp = n
# reverse number
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = int(temp / 10)
print(rev)

# palindrome check
if rev == n:
    print("Palindrome")
else:
    print("Not a palindrome")

# multiplication table of a number
a = int(input("Enter a number to find multiplication table:"))
for i in range(1, 11):
    print(i, "*", a, "=", i * a)

# sum and factorial
b = int(input("Enter a number to find sum and factorial:"))
if b < 0:
    print("Factorial not defined for negative numbers.")
else:
    total = 0
    factorial = 1
    for i in range(1, b + 1):
        total += i
        factorial *= i
    print("Sum:", total)
    print("Factorial:", factorial)

# basic arithmetic
a = int(input("Enter n1:"))
b = int(input("Enter n2:"))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Error! division by 0")

# check even or odd for n1
if a % 2 == 0:
    print("n1 is even")
else:
    print("n1 is odd")

# to find greatest of 3
c = int(input("Enter n3:"))
if a > b and a > c:
    print("n1 is larger")
elif b > a and b > c:
    print("n2 is larger")
else:
    print("n3 is larger")

# swap n1 and n2 using 3rd variable
d = a
a = b
b = d
print("After swap using 3rd variable:", a, b)

# swap n1 and n2 without using 3rd variable
a = a + b
b = a - b
a = a - b
print("After swap without 3rd variable:", a, b)

# F to c
f = int(input("Enter Fahrenheit:"))
c = (f - 32) * 5 / 9
print("Celsius:", c)