'''
import os
import requests
from bs4 import BeautifulSoup

os.chdir('F:\pythonenv\py27\jiandan')
res = requests.get('http://jandan.net/ooxx')
html = BeautifulSoup(res.text,'html.parser')
for index,each in enumerate(html.select('#comments img')):
	with open('{}.jpg'.format(index),'wb') as jpg:
		jpg.write(requests.get(each.attrs['src'],stream=True).content)
'''
import os
import requests
from bs4 import BeautifulSoup

os.chdir('F:\pythonenv\py27\jiandan')

index = 0
headers={'referer':'http://jandan.net/', 'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0'}

# Save picture
def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href'))-3: len(link.get('href'))]), 'wb') as jpg:
            jpg.write(requests.get(link.get('href')).content)
        index += 1


# default 5 pics
if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    for i in range(0, 5):
        save_jpg(url)
        url = BeautifulSoup(requests.get(url, headers=headers).text,"html.parser").find('a', {'class': 'previous-comment-page'}).get('href')