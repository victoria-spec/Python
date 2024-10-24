language ={} #--> empty

language ={"name":"python","version":3}
language ={"name":"python","version":3,}
#print(type(language))
#print(language)
#print(language["name"])
#print(language.get("years","Forgot to record"))

language.update({'name': 3, 'd': 4})
print(language)
language.setdefault('c', 3)  # This will add 'c': 3
language.setdefault('a', 10)  # This won't change 'a' si
print(language)

print(language.get(3))

#print(language.get("1","item does not exist"))

my_dict = {'a': 1, 'b': 2}
print(my_dict['b'])

print(language['key_not_exist'])


