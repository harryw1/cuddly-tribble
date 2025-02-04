import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

# print(students.duplicated())
# students.drop_duplicates()
# students.drop_duplicates(subset=["full_name"])
duplicates = students.duplicated()
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())