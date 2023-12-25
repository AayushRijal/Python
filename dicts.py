# a={} (Preferred way to make dictionaries)
# b=dict()
# print(type(a))
# print(type(b))

# a={'Ram':25,'Bill':40,'Rita':25}

#Dictionaries is heterogeneous. It can store multiple data types.
#Dictionary is mutable.

# c={'name':'Ram','Salary':'25000','is_married':False}

# f={'ram':25,'Bill':'50','Rita':25,'ram':32}
# print(f)
# print('ram' in grades)
# print('John' in grades)

# grades={'ram':25, 'Bill':82, 'Rita':33, 'ram':80}
# print(grades['ram'])

# grades['ram']=82

# print(grades)

# grades={'ram':25,'shyam':82,'rita':32}
# grades['rama']=28

# print(grades)

#Nested Dictionary

# info={'name':'ram', 'age':'28','address':{'city':'balaju','district':'KTM'}}
# info['name']
# info['age']
# info['address']['city']

# print(info)

grades={'ram':23,'shyam':44,'hari':34}
print(grades.key())
print(grades.values())
print(grades.items())
