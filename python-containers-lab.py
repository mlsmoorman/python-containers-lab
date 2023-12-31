# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.
print('========== Exercise 1 Solution ==========')

students = ['Melissa', 'Carlos', 'Jessi', 'Chris', 'Nichole']

print('Second Student: ', students[1])
print('Last Student: ', students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "[food goes here] is a good food".
print('========== Exercise 2 Solution ==========')

foods = 'lasagna', 'turkey', 'ham', 'salad', 'enchiladas', 'tamales'

for food in foods:
    print(f'{food.capitalize()} is a good food!')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

# Hint: Use the slice operator to select the last two foods
print('========== Exercise 3 Solution ==========')

last_two = foods[-2:]
for food in last_two:
    print(food)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
print('========== Exercise 4 Solution ==========')

home_town = {
    'city': 'Phoenix',
    'state': 'AZ',
    'population': '1.625 million'
}

print(f'I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.')


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
print('========== Exercise 5 Solution ==========')

for key, val in home_town.items():
    print(f'{key} = {val}')


# Exercise 6
# Create an empty list named cohort.

# Using a for loop to iterate over the students list.

# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

#  {
#    'student': 'Tina',
#    'fav_food': 'Cheeseburger'
#  }
# Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).
print('========== Exercise 6 Solution ==========')

cohorts = []

for idx, student in enumerate(students):
    cohorts.append({'student': {student}, 'fav_food': {foods[idx]}})

for cohort in cohorts:
    print(cohort)


# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.
print('========== Exercise 7 Solution ==========')

awesome_students = [f'{student} is awesome!' for student in students]

for awesome_student in awesome_students:
    print(awesome_student)

# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.
print('========== Exercise 8 Solution ==========')

list = []

for food in foods:
    if food.find('a') > -1:
        list.append(food)

for list_item in list:
    print(list_item)



