def reverse(s):
    s1=''
    for i in s:
        s1= i + s1
        print(s1)
    
    if s1==s:
        return True
    else: 
        return False
    
print(reverse("slice"))