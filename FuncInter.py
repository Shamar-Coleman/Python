#! 1.
#! Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30


#! 2
#! Iterate Through a List of Dictionaries
#!Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each
#!dictionary in the list and prints each key and the associated value. For example, given the following list:
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for index in range(len(students)):
        print(students[index])


iterateDictionary(students)


#! 3
#! Get Values From a List of Dictionaries
#! Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
#! and a key name, the function prints the value stored in that key for each dictionary.
#! For example, iterateDictionary2('first_name', students) should output:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(key_name, some_list):
    for index in some_list:
        print(index[key_name])


# code works with either 'las_name' or 'first_name'
iterateDictionary2('last_name', students)


#! 4
#!Iterate Through a Dictionary with List Values
#!Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
#!prints the name of each key along with the size of its list, and then prints the associated
#!values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, value in dojo.items():
        print(f"{len(value)} {key}")
        for i in range(len(value)):
            print(value[i])


printInfo(dojo)