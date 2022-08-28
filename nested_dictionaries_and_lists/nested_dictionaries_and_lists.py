# print("1.Update values in dictionary")
"""1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
2.Change the last_name of the first student from 'Jordan' to 'Bryant'
3.In the sports_directory, change 'Messi' to 'Andres'
4.Change the value 20 in z to 30"""
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[1]["last_name"] = "Bryant"
print(students)
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
z = [{'x': 10, 'y': 20}]
z[0]["you"] = 30
print(z)
"""2.Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
"""
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterate_dictionary(some_list):
    for i in some_list:
        print("first_name-"+i["first_name"]+","+"last_name-"+i["last_name"])
# iterate_dictionary(students)
"""Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

"""
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])


x = (iterateDictionary2("first_name", students))
y = (iterateDictionary2("last_name", students))
# Iterate Through a Dictionary with List Values
""""Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key]))+key)
        for i in some_dict[key]:
            print(i)
x = print_info(dojo)
