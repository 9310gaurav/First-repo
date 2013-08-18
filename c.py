from bs4 import BeautifulSoup
import codecs
file2=open('file.html','r')
soup = BeautifulSoup(file2)
file3=open('output.txt','w')
i=1
for string in soup.stripped_strings:
    if(i==1 or i==3):
      file3.write(string)
      file3.write('\n')
    if(i>14):
      if(i==15 or i==28 or i==39 or i==51 or i==63 or i==76 or i==88 or i==100 or i==112 or i==125 or i==135 or i==146 or i==158 or i==171 or i==184 or i==197 or i==211 or i==223 or i==237 or i==249 or i==260 or i==271 or i==283 or i==295 or i==308 or i==321 or i==334 or i==346 or i==359 or i==372 or i==384):
            file3.write('------------------------------------------------------------')
            file3.write('\n') 
            file3.write(string)
            file3.write('\n') 
      else:
             file3.write(string)
             file3.write('\n')       
    i=i+1
