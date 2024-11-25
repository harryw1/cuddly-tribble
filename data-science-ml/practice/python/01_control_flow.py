# Module 1
first_statement = True
second_statement = False
third_statement = 'No'

# Module 2
first_expression = True
second_expression = True 
third_expression = False

# Module 3
my_baby_bool = 'true'
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

# Module 4
user_name = 'Dave'

if user_name == "Dave":
  print("Get off my computer Dave!")

# Module 5
x = 20
y = 20

# Write the first if statement here:
if x == y:
    print("These numbers are the same")


credits = 120

# Write the second if statement here:

if credits >= 120:
    print("You have enough credits to graduate!")

# Module 6
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

# Module 7
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
elif (credits >= 120) or (gpa >= 2.0):
  print("You have met at least one of the requirements.")
else:
  print("You do not meet the requirements to graduate.")

# Module 8
statement_one = not (4 + 5 <= 9)
statement_two = not (8 * 2) != 20 - 4

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

# Module 8
grade = 78
if grade >= 90:
    print("A")
elif grade >=80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
