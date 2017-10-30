favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
# returns items 2-4, or indexes 1-3
slice1 = favorite_things[1:4]
# returns last 2 items, index 5 onward
slice2 = favorite_things[5:]

# creates a new identicle list and sorts it
sorted_things = favorite_things[:]
sorted_things.sort()

# returns first 4 items in a list
def first_4(iterable):
    return iterable[:4]

# returns all odd indexes from index 1 onward
def odds(iterable):
    return iterable[1::2]

# returns all even indexes in a reverse fashion, starting from the last even index
def reverse_evens(iterable):
    if len(iterable) % 2 == 0:
        return iterable[-2::-2]
    else:
        return iterable[-1::-2]

# takes a string and returns the first half of the string in lower case and the upper half of the string in upper case using list slices
def sillycase(string):
    length = len(string) // 2
    return string[:length].lower() + string[length:].upper()