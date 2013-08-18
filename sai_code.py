import requests
from bs4 import BeautifulSoup

url = "http://cse.iitkgp.ac.in/faculty.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

cnt = 0
cnt1 = 0
f = open('workfile', 'w')
for string in soup.stripped_strings:
    doc = str(string)
    if cnt<14 or cnt1>29:
        cnt = cnt+1
        continue 

    if doc[:8] == 'Personal':
        continue
    f.write((string))
    if doc[:8] == 'Research':
        continue
    elif doc[-1] == '.':
        f.write('\n\n')
        cnt1 = cnt1+1
    elif doc[-1] == ':':
        continue
    else:
        f.write(' | ')

f.close()
f = open('workfile', 'r')
for line in f:
    print line,

    



  







