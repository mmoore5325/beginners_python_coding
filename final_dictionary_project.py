def teachers(dictionary):
  i = 0
  for key in dictionary.keys():
    i += 1
    
  print(i)

def num_courses(dictionary):
  i = 0
  for value in dictionary.values():
    if isinstance(value, list):
      for courses in value:
        i += 1
    else:
      i += 1
  print(i)
  
def courses(dictionary):
  courses = list()
  for value in dictionary.values():
    if isinstance(value, list):
      for classes in value:
        courses.append(classes)
    else:
      courses.append(value)
      
  print(courses)
  
def most_courses(dictionary):
  number_of_courses = dict()
  for key in dictionary.keys():
    if isinstance(dictionary[key], list):
      print(key, len(dictionary[key]))
    else:
      print(key, "1")
  #  for key in dictionary.keys():
#      number_of_courses[key] = 
#  for key in dictionary.keys():
#    if key in number_of_courses[key]
#      number_of_courses[key] = len(dictionary[key])
#      print(number_of_courses)
#    for value in dictionary.values():
#      print(key, value)
#      if isinstance(value, list):
#        for classes in value:
#          number_of_courses[key] += 1
#      else:
#        number_of_courses[key] += 1
#        
  print(number_of_courses)
dictionary = {"a": ["python", "cyclops"], "b":"c++", "c":["c", "e", "f"], "d":"ruby", "e":"javascript"}
teachers(dictionary)
num_courses(dictionary)