from bs4 import BeautifulSoup
import codecs

file1=open('source.html','r')
soup=BeautifulSoup(file1)

for i in range(0,4):
    soup.br.decompose()



file2=codecs.open('output.txt','w','utf-8')


tag=soup.center

tag1=tag.contents[1]

for j in range(3,93):
    if(j%3==0):
        tag2=tag1.contents[j]
        for i in range(3,22):
            if(i==3):
                tag3=tag2.contents[i].b
                for child in tag3.children:
                    file2.write(child)
                    file2.write("\n")
            elif(i==9):
                tag3=tag2.contents[i].a
                for child in tag3.children:
                    file2.write(child)
                    file2.write("\n")
            elif(i==21):
                tag3=tag2.contents[i].a
                file2.write(tag3['href'])
                file2.write("\n")
            elif(i%2!=0):
                tag3=tag2.contents[i]
                for child in tag3.children:
                    file2.write(child)
                    file2.write("\n")
        tag5=tag1.contents[j+2].i
        for child in tag5.children:
            file2.write(child)
            file2.write("\n") 
        file2.write("-----------------------------------------------------------------------\n")           
file2.close()
        

            



