##a=input("")
##for i in range(len(a)):
##    for j in a:
##        for k in a:
##            if j.isdigit() and k.isdigit():
##                print(a(j)+a(k))
##            
##        

##def sum_digits(digit):
##    return sum(int(x) for x in digit if x.isdigit())
##sum_digits(input(""))

##import bs4 as bs
##from pprint import pprint
##import urllib.request
##
##sauce=urllib.request.urlopen('https://www.lpu.in').read()
##soup=bs.BeautifulSoup(sauce,'lxml')
##print(soup.title.text)
##
##for url in soup.find_all('a'):
##    pprint(url.get('href'))


l=list(input())
n=[]
sum=0
for i in range(len(l)):
    if(l[i].isdigit()):
        n.append(l[i])
    else:
        if len(n)!=0:
            s="".join(n)
            sum+=int(s)
            n.clear()

if len(n)>0:
    s="".join(n)
    sum+=int(s)
    n.clear()

temp=0
while len(list(str(sum)))!=1:
    while sum!=0:
        temp+=sum%10
        sum=int(sum/10)
    sum=temp
    temp=0
print(sum)
