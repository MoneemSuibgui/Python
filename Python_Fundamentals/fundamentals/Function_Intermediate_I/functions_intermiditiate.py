x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#1- Update Values in Dictionaries and Lists
#1
x[1][0]=15
print (x)

#2
students[0]["last_name"] = "Bryant"
print(students)

#3
sports_directory ["soccer"][0] = "Andres"
print(sports_directory)

#4
z[0]["y"] = 30
print (z)
print("-"*12)
#2- Iterate Through a List of Dictionaries
def iterateDictionary(some_list) : 
    for dico in some_list :
        for key, value in dico.items():
            print (f"{key} - {value}", end=", ")
        print("")
iterateDictionary(students)
print("-"*12)
#3- Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range (0, len(some_list)):
        print (some_list[i][key_name])

iterateDictionary2('last_name', students)

#4- Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for keys, values in some_dict.items() :
        print("-"*12)
        print (f"{len(values)} {keys.upper()}")
        for value in values :
            print (value)
        print("")
printInfo (dojo)