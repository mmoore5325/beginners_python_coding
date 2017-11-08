def multiply(*nums):
    store = []
    for num in nums:
        store.append(num)
        
    i = 2
    total = store[0] * store[1]
    while i < len(store):
        total *= store[i]
        i+=1

    return(total)
multiply(1,2,3,4,5)