# Write a Python function to find the maximum of three numbers.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = 30*1
num2 = 30*2
num3 = 30*3
result = maximum(num1, num2, num3)
print("The maximum number is:", result)



