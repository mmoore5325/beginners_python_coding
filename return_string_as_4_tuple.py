# Looking for any string returned lowercased, uppercased, titlecased(not capitalized as I made the mistake of), and reversed 
def stringcase(string):
    print(string.lower()) # lowercased
    print(string.capitalize()) # first word capitalized
    print(string.upper()) # All upper cased
    print(string.title()) # First letter of every word capitalized
    print(string[::-1]) # Word returned in reversed using slice
    reversed = []
    x = (len(string)-1)

    while x >= 0:
        reversed.append(string[x])
        x-=1

    reversed_word = "".join(reversed)

    # This reversed method is much shorter than the one starting on line 6 through 13, D'oh!!
    reversedd = string[::-1]
    print(reversedd)
    return(string.lower(), string.upper(), string.title(), string[::-1])
  
stringcase("SHITballs oF fIRe")