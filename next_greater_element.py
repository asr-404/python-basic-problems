def next_greater_element(arr):
    n = len(arr)
    res = [-1]*n
    stk=[]

    for i in range(n-1,-1,-1):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()
        
        if stk:
            res[i]=arr[stk[-1]]
        
        stk.append(i)

    print(res)

arr=[6, 8, 0, 1, 3]
print(arr)
next_greater_element(arr)