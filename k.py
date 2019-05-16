#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: seair
# @Date:   2019-05-14 22:46:00
# @Last Modified by:   Seair
# @Last Modified time: 2019-05-16 22:24:09

import os
import time
import codecs



def repair(old, new):
	Last = ''
	for line in old:
		k1 = line.find('你的答案')!=-1
		k2 = line!='\n'
		k3 = Last!='\n'
		if not k1 and k2:
			new.write(line)
			pass
		if k1 and k3:
			new.write(line)
			new.write('\n')
			pass
		Last = line
		pass
	pass


def getAnswer(file):
	k2 = 0
	k3 = 0
	for line in file:
		k3 += 1
		k1 = line.find('你的答案')!=-1
		if k1:
			k2 += 1
			pass
		pass
	file.seek(0, 0)
	return (k2, k3)
	pass


courses = ['乒乓球', '健美操', '太极拳', '排球', '排舞', '散手', '校园定向', '气排球', '瑜伽', '社交舞', '篮球', '网球', '羽毛球', '艺术体操', '足球', '跆拳道']

# courses_file = []
for course in courses:
	course = './{}/{}.txt'.format(course, course)
	if os.path.exists(course):
		os.remove(course)
		pass
	pass


folder_path = './Z'
files = os.listdir(folder_path)
for file in files:
	course = file[file.find('-')+1:file.find('理论')]
	course = './{}/{}.txt'.format(course, course)
	with codecs.open(course, 'a', 'utf-8') as course:
		old = codecs.open('{}/{}'.format(folder_path, file), 'r', 'utf-8')
		# course.write(old.read())
		repair(old, course)
		old.close()
		pass
	pass

allMsg = []
name = './总题库.txt'
AllQuestion = codecs.open(name, 'w', 'utf-8')
for course in courses:
	msg = {'name':course, 'sum':0, 'size':0, 'line':0}
	course = './{}/{}.txt'.format(course, course)
	if os.path.exists(course):
		msg['size'] = os.path.getsize(course)//1024
		course = codecs.open(course, 'r', 'utf-8')
		(msg['sum'], msg['line']) = getAnswer(course)
		AllQuestion.write(course.read())
		AllQuestion.write("\n\n")
		course.close()
		pass
	allMsg.append(msg)
	pass
AllQuestion.close()




AllQuestion = codecs.open(name, 'r', 'utf-8')
(k2, k3) = getAnswer(AllQuestion)
AllQuestion.close()

msg = {'name':'总题库', 'sum':k2, 'size':os.path.getsize(name)//1024, 'line':k3}
allMsg = [msg] + allMsg

# print('题目总数:', k2)
# exit(0)


s = []
for msg in allMsg:
	it = '[{}]({}) | {}kb | {} | {}'.format(
		msg['name'], 'http://im.s8cm.cn/{}.txt?attname='.format(msg['name']),
		msg['size'], msg['line'], msg['sum'])
	# print(it)
	s.append(it)
	pass

s = '\n'.join(s)
# print(s)

Last = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# print('最后更新时间:', Last)


README = '''# QuestionBank

创高体育题库-四川大学

## 说明

本仓库致力于收集四川大学体育理论考试题目  

地址：<a href="https://gitee.com/cherry-l/QuestionBank" target="_blank">码云</a> or <a href="https://github.com/s8cm/QuestionBank" target="_blank">Github</a>

最后更新时间: {} 

请滑到底部查看使用帮助

* * *

### 题库详细信息

注：点击蓝色字体可下载  

题库 | 大小 | 行数 | 题数
-|-|-|-
{}  


* * *

### 使用帮助

可将题库下载到本地，PC端用记事本，安卓端推荐用<a href="https://www.coolapk.com/apk/bin.mt.plus" target="_blank">MT管理器</a>  

本地搜索是最快的，当然也提供网页搜索：

<a href="http://i.s8cm.cn/" target="_blank">i.s8cm.cn</a>
 or 
<a href="http://im.s8cm.cn/" target="_blank">im.s8cm.cn</a>

### 联系方式

QQ <a href="http://wpa.qq.com/msgrd?v=3&uin=1328357049&site=qq&menu=yes" target="_blank">1328357049</a>  

### 致谢

感谢国家:)

'''.format(Last, s)


print(README)

Modified = codecs.open('./README.md', 'w', 'utf-8')
Modified.write(README)
Modified.close()




