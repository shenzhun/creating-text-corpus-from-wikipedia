import re
import sys

f = open('num_tmp', 'rb').read()
rc = re.compile('split-enwiki-part.*')
split_xml_files = re.seach(rc, f)

for xml_file in split_xml_files:
	f1 = open(xml_file, 'rb').read()
	list = re.findall('<page>(.*?)</page>', f1, re.S)
	counter = 0
	for i in list:
		counter = counter + 1
		with open('test.'+str(counter), 'w') as fw:
			fw.write(i)

