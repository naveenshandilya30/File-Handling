#Question 1

f=open("file.txt",encoding='utf8')
a=(f.readlines())
a.reverse()
n=int(input("No. of last lines to read: "))
for i in range(0,n):
    print(a[i])
    f.close()


#Question 2


a="Atticus"
f=open("file.txt","r")
b=f.read()
m=b.split()
print(b.count(a))



#Question 3

f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("file3.txt","w")
c.writelines(a)

#Question 4


i=0
f=open("file1.txt","r")
a=(f.read())
b=open("file2.txt","r")
c=(b.read())
d= open("file4.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()


#Question 5

l=[]
global str
j=[]
import json
import random
for i in range(0,10):
    l.append(random.randint(1,10))
f=open("file2.txt","w")
for t in l:
    h="".join(str(t))
    f.write(h)
f.close()
d=open("file2.txt","r")
a=d.read()
for x in a:
    if(x.isdigit()):
        m="".join(x)
        j.append(m)
j.sort()
c=open("file5.txt","w")
c.write(str(j))

