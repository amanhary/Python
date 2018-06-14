newList=[]
def fun(l):
    index=3-1
    beg=0
    size=(len(l))

    while size>0:
        beg=(index+beg)%size
        newList.append((l.pop(beg)))
        size=size-1

l=list(map(int,input("enter the elements in the lists:\n").split()))
fun(l)
print(newList)
