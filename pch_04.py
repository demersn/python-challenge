# http://www.pythonchallenge.com/pc/def/linkedlist.php
# import webbrowser
import urllib.request
import re
# We see a picture of 2 people using a SAW (chainsaw)
# title says, follow the chain
# from the link, we get nothing=12345
# the page shows 'the next nothing is 44827'
# Source code shows:
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never end.
# 400 times is more than enough
# We now understand that we have to scan the number and follow the chain

nothing = '12345'
for i in range(400):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing) as response:
        html = response.read()
        nnext = str(html, 'utf-8')  # byte string to string
        nnext = re.findall('\d+', nnext)  # only take digits
        if not nnext:  # Check if list of numbers is empty
            nothing = int(nothing)/2  # Curve ball
        else:
            nothing = nnext[-1]  # Take last 'nothing' only (2nd curve ball)
        print(nothing)
# By looking at a .5 result, we find the text 'peak.html' with the number
# 66831. Not sure how to stop it when we find a link.
