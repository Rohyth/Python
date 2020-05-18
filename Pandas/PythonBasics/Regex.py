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
pattern = re.compile("[1-100]")
result = pattern.search(ntxt)
result
