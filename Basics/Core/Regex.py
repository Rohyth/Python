#Regex 

import re

text = "Hello there , My Name is Rohyth"
pattern = re.compile("Hello there , My Name is Rohyth")

result = pattern.search(text)
result


pattern = re.compile("[a-z]")
result = pattern.search(text)
result

pattern = re.compile("[A-Z]")
result = pattern.search(text)
result

ntxt = "Hi, my number is 7290845646"
pattern = re.compile("[0-9]")
result = pattern.search(ntxt)
result

# Extract a email address from a string

nwStr = 'Hey there, my id is Rohitratawal@gmail.co.in . Isnt it Amazing . other id is NupurSinha@gmail.co.in'
pattern = re.compile("@")

res = pattern.search(nwStr)
res

pattern = re.compile("[a-zA-Z0-9]+@+[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.+[a-zA-Z0-9]+")
res = pattern.findall(nwStr)
res



