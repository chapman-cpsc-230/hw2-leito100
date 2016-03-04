b = float(input("Please enter a decimal number not equal to 1.0:"))
n = int(input("please enter an integer"))
x = 1 + b
for i in range(2, n+1):
    x += b** i
j = (b ** (n+1))/ (b-1)
print("sum", x)
print("sum", j)
