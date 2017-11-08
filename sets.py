COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(topics):
  course = []
  for key, value in COURSES.items():
    if value.intersection(topics):
      course.append(key)
  return(course)

def covers_all(arg):
    course = []
    for key, value in COURSES.items():
        if arg.issubset(value):
            course.append(key)
    return(course)
#    return(course)
  
#topics = {"variables"}
#covers(topics)

all_topics = {"Ruby", "strings", "floats",
              "integers", "functions", "input"}

covers_all(all_topics)