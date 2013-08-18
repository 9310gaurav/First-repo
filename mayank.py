from bs4 import BeautifulSoup
import codecs

file=open('name.html','r')
file1=codecs.open('output.txt','w','utf-8')
soup=BeautifulSoup(file)

tag=soup.table
for k in range(3,93):
    if(k%3==0):
       tag1=tag.contents[k]
       tag3=tag.contents[k+2]
       j=3

       tag2=tag1.contents[j].b
       for child in tag2.children:
           print("Name: %s\n"%child)
           file1.write("Name: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Designation: %s\n"%child)
           file1.write("Designation: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("phD: %s\n"%child)
           file1.write("phD: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j].a
       for child in tag2.children:
           print("office room no.: %s\n"%child)
           file1.write("office room no.: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Phone No.(office): %s\n"%child)
           file1.write("Phone No.(office): %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Phone No.(res): %s\n"%child)
           file1.write("Phone No.(res): %s\n"%child)
       
       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Phone No.(res 2): %s\n"%child)
           file1.write("Phone(res 2): %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Email: %s\n"%child)
           file1.write("Email: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j]
       for child in tag2.children:
           print("Quarters: %s\n"%child)
           file1.write("Quarters: %s\n"%child)

       j=j+2
       tag2=tag1.contents[j].a
       for child in tag2.children:
           print("Webpage: ")
           print(tag2['href'])
           print("\n")
           file1.write("Webpage: ")
           file1.write(tag2['href'])
           file1.write("\n")

       tag4=tag3.contents[0].i
       for child in tag4.children:
           print("Research Areas: %s\n"%child)
           file1.write("Research Areas: %s\n"%child)


       print("------------------------------------------------------\n")
       file1.write("-----------------------------------------------------\n")
 
file1.close()
