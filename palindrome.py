def palindrome(num):
    original = num
    sum=0
    while num > 0:
        digit = num%10
        sum = sum *10 + digit
        num = num //10

    return original == sum

print(palindrome(1231))