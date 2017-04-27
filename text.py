import re
test = 'abc'
nnext = re.findall('\d+', test)
nnext = nnext[0]
print(nnext.isdigit())
