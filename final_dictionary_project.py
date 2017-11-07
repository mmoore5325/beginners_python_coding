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
  teacher = ""
  classes = 0
  for key in dictionary.keys():
    if isinstance(dictionary[key], list):
      number_of_courses[key] = len(dictionary[key])
    else:
      number_of_courses[key] = 1
  for key, value in number_of_courses.items():
    if value > classes:
      teacher = key
      classes = value
  print(number_of_courses)
  print(teacher, classes)
  
def stats(dictionary):
  teachers_class_list = list()
  i = 0
  for key, value in dictionary.items():
    teachers_class_list.insert(i, [key])
    if isinstance(value, list):
      teachers_class_list[i].append(len(value))
    else:
      teachers_class_list[i].append(1)
    i+=1
  
  print(teachers_class_list)
  return(teachers_class_list)
    

dictionary = {"John Love": ["python", "cyclops"], "Emmett Vernon":"c++", "Jacob Carroll":["class_of fixing stuff", "do it yourself idiot", "handyman"], "Michael Moore":["ruby", "calculus", "physics", "meaning of life"], "Maxx Maxx":["csss", "Phython"]}
#teachers(dictionary)
#num_courses(dictionary)
#courses(dictionary)
#most_courses(dictionary)
stats(dictionary)