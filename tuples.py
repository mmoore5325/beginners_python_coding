def multiply(*nums):
  store = []
  for num in nums:
    store.append(num)
    print(store)
  print(len(store))
  i = 2
  total = store[i] * store[i+1]
  while i < len(store):
    total *= store[i]
    i+=1
    print(total)
    
multiply(2,2,2,2,2)