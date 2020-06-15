# trick One -------------------

condition = True

if condition:
    x=1
else:
    x=0
    
print(x)

'Alternative ---------------'

condition = False
x = 1 if condition else 0
print(x)

# Trick two --------------------------------------------

lst = ['Rohyth','Ravi','Ritu','Avi','Aditya']

index = 0
for name in lst:
    print(index, name)
    index += 1
    
    
'Alternamtive -------------------'

for index, name in enumerate(lst):
    print(index, name)
    
'-------------------------------------------------------------'
# Trick three-------------------------------------------------

l1 = ['Rohit', 'Ravi','Ritu']
l2 = ['Python','Sql','VBA']

'Use Zip function to unpack from multiple list at once------'

for name,program in zip(l1,l2):
    print(name , program )



'--------------------------------------------------------'
# Trick four 

'unpacking-------------------------'

a,b = (1,2)
print(a)
print(b)


a,b ,*c = (1,2,3,4,5,6)
print(a)
print(b)
print(c)

a, b, *c,d = (1,2,3,6,5,4,7,8)
print(a)
print(b)
print(c)
print(d)


'use _ to ignore '
a, b, *_,d = (1,2,3,6,5,4,7,8)
print(a)
print(b)

print(d)





















