import re
import sys


f1 = open(sys.argv[1], 'rb').read()
list = re.findall('<text(.*?)</text>', f1, re.S)
for i in list:
    i = '\n<text ' + i + '</text>\n'
    with open(sys.argv[1]+'.xmltext', 'a') as fw:
	fw.write(i)

