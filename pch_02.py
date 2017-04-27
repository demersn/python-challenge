# http://www.pythonchallenge.com/pc/def/ocr.html
import webbrowser
with open('F:\Git\python-challenge\pch_02.txt', 'r') as myfile:
    code = myfile.read()
decode = ''
matrix = []
for i in range(len(code)):
    if ord(code[i]) >= 97 and ord(code[i]) < 122:
        decode = decode+code[i]
        matrix.append(i)
print(decode)
# print(matrix)
webbrowser.open('http://www.pythonchallenge.com/pc/def/%s.html' % decode)
