import random
import pandas
# list comprehension
# creating list from a list
# it works with any sequence for example string 

# list comprehension example
# numbers = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [i + 10 for i in numbers]
# print(new_list)
# with condition
# new_list = [i for i in numbers if i % 2 == 0]
# print(new_list)

# dictionary comprehension example
scores = { "Alex": 90, "Bob": 20, "Charlie": 60, "Dave": 70 }
student_dict = {
   "student": ['Angela', "James", "Lily"],
   "score": [56, 80, 34]
}
# new_scores =  { key: random.randint(80, 100) for key in scores.keys()}
# print(new_scores)

# passed_students = { key: value for (key, value) in scores.items() if value >= 60}
# print(passed_students)

df = pandas.DataFrame(student_dict)
for (key, value) in df.iterrows():
   print(value)