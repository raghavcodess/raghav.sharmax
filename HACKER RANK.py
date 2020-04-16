n=int(input(""))
list=[]
for x in range(0,n):
    a=input("")
    if(len(a)==10):
        e=a[-1]
        i=a[-3]
        e=int(e)
        i=int(e)
        list.insert(i,e)
        
    elif(len(a)==3):
        list.pop()
    elif(len(a)==5):
        print(list)
    elif(len(a)==4):
        list.sort()
    elif(len(a)==7):
        list.reverse()
    elif(len(a)==8 and a[0]=='a'):
        e=a[-1]
        e=int(e)
        list.append(e)
    elif(len(a)==8 and a[0]=='r'):
        e=a[-1]
        e=int(e)
        list.remove(e)
    elif(len(a)==11):
        e=a[-2]+a[-1]
        e=int(e)
        i=a[-4]
        i=int(i)
        list.insert(i,e)
        
    
    