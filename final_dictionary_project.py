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
dictionary = {"a": ["python", "cyclops"], "b":"c++", "c":["c", "e", "f"], "d":"ruby", "e":"javascript"}
teachers(dictionary)
num_courses(dictionary)
courses(dictionary)