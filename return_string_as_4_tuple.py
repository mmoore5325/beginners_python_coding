def stringcase(string):
      print(string.lower())
  print(string.capitalize())
  print(string.upper())
  print(string.title())
  reversed = []
  x = (len(string)-1)

  while x >= 0:
    reversed.append(string[x])
    x-=1

  reversed_word = "".join(reversed)

  # This reversed method is much shorter than the one starting on line 6 through 13, D'oh!!
  reversedd = string[::-1]
  print(reversedd)
#  print(reversed_word)
  
stringcase("SHITballs oF fIRe")