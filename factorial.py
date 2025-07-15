def factorial(num):
    if num < 0:
        return "no factorial for negative numbers"
    elif num ==  0:
        return 1
    sum=1
    for i in range(num, 0, -1):
        sum*=i

    return sum

print(factorial(10))