
movie={
    'title':'gone with the wind',
    "releasse_year":1994,
    "director": 'Mark Golden',
    'producer': 'John Gale',
    "leading_actors": ["Actor1","Actor2","Actor3"],
    "ganre": "romance",
    "runtime_minutes":206,
    "plot_summary":("Movie description is this move the is taking place"
                    " in Italy"
                    " sadadada"
                    " asdasdasdad")
}



#print(movie)
keys =movie.keys()
values =movie.values()
print(values)
for key in keys:
    print(key,movie[key],sep="=")

print(movie.items())    
