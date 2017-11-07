def word_count(string):
  dictionary = dict()
  splits = string.lower().split()
  print(splits)
  for word in splits:
    dictionary[word] = 0
  for word in splits:
    for key in dictionary.keys():
      if word == key:
        dictionary[word] +=1
  print(dictionary)
  return dictionary

  

word_count("I i I HaVE HAVE have A a A A a A Rea REA rea real b b B BAD stu STu STUT STUTtering stuttering Pro PRO pRo Problem")
word_count("I do not like it Sam I Am")