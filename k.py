#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: seair
# @Date:   2019-05-14 22:46:00
# @Last Modified by:   Seair
# @Last Modified time: 2019-05-14 23:04:35

import os
import codecs


folder_path = './Z'

AllQuestion = './AllQuestion.txt'


file = 'html-跆拳道理论考试-141011020.txt'

file = file[file.find('-')+1:file.find('理论')]

print(file)
fileSet = set([])
fileSet.add(file)
print(list(fileSet)[0])

exit(0)

AllQuestion = codecs.open(AllQuestion, 'w', 'utf-8')

files = os.listdir(folder_path)
fileSet = set([])

for file in files:
	(file_name, extension) = os.path.splitext(file)
	if extension=='.txt' and file.find('html')!=-1:
		fileSet.add(file[file.find('-')+1:file.find('理论')])
		with codecs.open('{}/{}'.format(folder_path, file), 'r', encoding='utf-8') as f:
			t = f.read()
			# t = str(t, encoding='utf-8')

			# print(t)
			# break
			# t = str()
			# print(len(t))
			AllQuestion.write(t)
			pass
		print(file)
		pass
	pass


AllQuestion.close()


