# http://www.pythonchallenge.com/pc/def/map.html
import webbrowser

# Take letter and use the +2 letter: K->M, O->Q, E->G
mapfrom = 'abcdefghijklmnopqrstuvwxyz'
mapto = 'cdefghijklmnopqrstuvwxyzab'
mapp = str.maketrans(mapfrom, mapto)
a = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

print(a.translate(mapp))
ans = 'map'.translate(mapp)
print(ans)
webbrowser.open('http://www.pythonchallenge.com/pc/def/%s.html' % ans)
