# http://www.pythonchallenge.com/pc/def/equality.html
import webbrowser
with open('F:\Git\python-challenge\pch_03.txt', 'r') as myfile:
    code = myfile.read()
# On utilisera la fonction .isupper()
candle = ''
for i in range(len(code)):
    if code[i].isupper() is True and \
       code[i+1].isupper() is True and \
       code[i+2].isupper() is True and \
       code[i+3].isupper() is False and \
       code[i+4].isupper() is True and \
       code[i+5].isupper() is True and \
       code[i+6].isupper() is True:
        if code[i-1].isupper() is False and \
           code[i+7].isupper() is False:
            candle = candle+code[i+3]
print(candle)
webbrowser.open('http://www.pythonchallenge.com/pc/def/%s.html' % candle)
