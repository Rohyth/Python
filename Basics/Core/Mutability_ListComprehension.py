"""
@author: rohyth
"""

#mutability means changability
# List,dicts are mutable 
# Tuples is immutable


#list Comprehension--------------------------------

names = ['Rohyth','Ravi','Riu','Nupur']

l = []

for name in names:
    l.append(name)

print(l)


'''Comprehension---------------------------------
'''

M = [name for name in names]
M

#New example ------------------------------------

l = []

for name in names:
    l.append(name + ' is great')
print(l)


print([name + ' is Crazy' for name in names])

#--------------------------------------------------------

movies = {"RHtdm":10,"American Pie":4,"Planet of Apes":9}

N = []
for movie in movies:
    if movies[movie] > 5:
        N.append(movie)

N

# Now list comprehension

print(  [m for m in movies if movies[m] > 5 and movies[m] < 10] )





















