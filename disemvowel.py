def disemvowel(word):
  vowels = ["a", "e", "i", "o", "u"]
  new_word_list = list(word)
  for vowel in vowels:
    while vowel in new_word_list:
        new_word_list.remove(vowel)
#  return ''.join(new_word_list)
  print(new_word_list)        
  final_word = ''.join(new_word_list)
  print(final_word) 
  
word = "Thishaseveryvowulyesispelledutwrong"        
disemvowel(word)
        