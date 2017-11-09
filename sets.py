#### MY NOTES ON SETS ####
# find the difference between 2 sets
# set1.difference(set2)
# set1 - set2
# set2.difference(set1)
# set2 - set1

# Unique to each side
# set1 ^ set2
# set1.symmetric_difference(set2)

# Find items that are common from each side
# set1.intersection(set2)
# set1 & set2

# to join them
# set1.union(set2)
# set1 | set2

# Same as update but set1.update(set2) permanently changes set1


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