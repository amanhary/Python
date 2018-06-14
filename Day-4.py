##Append,Extend,Insert(),Pop
##
## l=['abc',1,10,20]
##>>> l
##['abc', 1, 10, 20]
##>>> a=[7,8,9]
##>>> l.append(a)
##>>> l
##['abc', 1, 10, 20, [7, 8, 9]]
##>>> a.extend([4,5,6])
##>>> a
##[7, 8, 9, 4, 5, 6]
##>>> l+[11,12]
##['abc', 1, 10, 20, [7, 8, 9, 4, 5, 6], 11, 12]
##>>> a.insert(0,0)
##>>> a
##[0, 7, 8, 9, 4, 5, 6]
##>>> a.insert(3,'aman')
##>>> a
##[0, 7, 8, 'aman', 9, 4, 5, 6]

##>>> a.count(4)
##1
##>>> l.clear()
##>>> l
##[]
##>>> l.extend([21,2,34,12,22,10])
##>>> l
##[21, 2, 34, 12, 22, 10]
##>>> l.sort()
##>>> l
##[2, 10, 12, 21, 22, 34]
##l.sort(reverse=True)
##l.reverse()
##l[-1::-1]

##WAP tp print square of numbers in range 0-9
##l=[]
##for i in range(10):
##    l.append(i**2)
##print (l)

##print([i**2 for i in range(10)])
##
##l=[]
##def details(name,marks):
##    print(name,marks)
##    if marks>=81 and marks<=100:
##        print("A+")
##    elif marks>=70 and marks<=80:
##        print("A")
##    else:
##        print("low grades")
##details(input("Enter Name: "),int(input("Enter Marks:")))

##l=[]
##for i in range(int(input("Enter the number of students: "))):
##    name=input("Enter Name:\n")
##    marks=int(input("Enter the marks:\n"))
##    grade=''
##    if marks>=81 and marks<=100:
##        grade="A+"
##    elif marks>=70 and marks<=80:
##        grade="A"
##    else:
##        grade="low grades"
##    l.append([name,grade])
##print(l)

##>>> chr(50)
##'2'
##>>> chr(97)
##'a'
##>>> ord('A')
##65
##>>> ord('a')
##97

##l=[]
##for i in range(int(input("Enter the number of alphabets: "):
##    alpha=input()
##    value=ord(alpha)
##    l.append([alpha,value])
##print(l)
    
##import string
##for i in string.ascii_lowercase:
##    print(ord(i))

##l=[]    
##n=[1,2,3,4,5]
##m=['a','b','c']
##for i in n:
##    for j in m:
##        l.append([i,j])
##print(l)


#LIST_COMPREHENSION
##[print([i,j]) for i in[1,2,3,4] for j in['a','b','c']]
##
##l=[x for x in range(0,20) if x%3==0]
##print(l)


#DICT_COMPREHENSION--
##dict_comp={x:chr(65+x) for x in range(1,11)}
##print(dict_comp)
##
###SET_COMPREHENSION--
##set_comp={x**3 for x in range(10) if x%2==0}
##print(set_compz)

#LIST_COMPREHENSION AND GENERATOR_EXPRESSION
##from sys import getsizeof
##my_comp={x*5 for x in range(1000)}
##my_gen=(x*5 for x in range(1000))
##print(getsizeof(my_comp))
##print(getsizeof(my_gen))

##for i in range(1,20):
##    if i==10:
##        break
##    else:
##        print(i)
##for i in range(1,10):
##    if i==5:
##        continue
##    else:
##        print(i)
##for i in range(1,10):
##    if i==5:
##        pass

import string
k=list(input())
l=set(k)








