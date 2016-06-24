import os
path = 'F:\pythonenv\Downloader\YouDown'
os.chdir(path)
filelist = os.listdir(path)
matchlist = [filename for filename in filelist if filename.endswith('.mp4')]
nmatchlist = map(lambda i: i + '\n', matchlist)
strn = ''.join(nmatchlist)
with open('list.txt', 'w') as hand:
    hand.write(strn)
