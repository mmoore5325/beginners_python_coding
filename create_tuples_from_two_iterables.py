# it said assume both iterables are the same length, so this only works on mutable
# objects that, when measured, are the same length
def combo(iterable, iterable2):
    alist = []
    i = 0
    print(len(iterable))
    print(len(iterable2))
    if len(iterable) >= len(iterable2):
      print("iterable is greater than or equal to iterable2")
      while i < len(iterable):
        alist.insert(i, (iterable[i], iterable2[i]))
        i+=1
  ##### THE ACCEPTABLE ANSWER IS EVERYTHING ABOVE THIS LINE #########
    # else:
    #   while i < len(iterable2):
    #     alist.insert(i, (iterable[i], iterable2[i]))
    #     i+=1
    # print(alist)    
    
iterable = ["a", "b", "c", "d", "e"]
iterable2 = ["f", "g", "h", "i", "j"]

combo(iterable, iterable2)