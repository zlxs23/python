# _*_coding:utf-8_*_

import os
import re

# Read HTML to Get Record
# <!-- 可设置 textarea cols rows 设置 不可被拖动修改大小 放屁 不能实现 -->

pattern = re.compile(r'<!-- (.*?) -->')
folder = 'F:\\Save\\Internship\\Record'
os.chdir(folder)
for htmlfile in os.listdir(folder):
	if os.path.isfile(htmlfile):
		with open(htmlfile) as html:
			for line in html.readlines():
				line = line.lstrip()
				if line.find('<!--') != -1:
					mat = re.match(pattern, line)
					if mat != None:
						print(mat.group(1))
						# 需要处理 <!--