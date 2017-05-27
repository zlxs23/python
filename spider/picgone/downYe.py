# ——*——coding:utf-8_*_

import urllib
import urllib2
import re
import os

imgDir = 'F:\\Save\\python\\spider\\picgone\\img'
url = 'http://is02.picsgonewild.com/2016/07/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0'
cookies = '__cfduid=d52bf4dac5695c9a6f371008a6f46aac81471760309; __utma=166927142.1615340706.1471760313.1471760313.1471770119.2; __utmc=166927142; __utmz=166927142.1471760313.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=221152025.241494734.1471760610.1471760610.1471770262.2; __utmc=221152025; __utmz=221152025.1471760610.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=166927142.10.10.1471770119'
headers = {'User-Agent': user_agent, 'Cookie': cookies}
day = '10'

try:
	request = urllib2.Request(url+day, headers=headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<a href=.*?>(.*?)</a>', re.S)
	items = re.findall(pattern, content)
	for item in items:
		print item
		if 'th' not in item and 'md' not in item and 'jpg' in item:
			imgContent = urllib2.urlopen(urllib2.Request(url+day+'/'+item, headers=headers))
			f = open(imgDir+os.sep+item, 'wb')
			f.write(imgContent.read())
			print 'Saved'
			f.close()
except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason