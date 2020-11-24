type1=['    +','+---+','+   +']
type2=['    |','|    ','|   |']
uppper={'0':1,'1':0,'2':1,'3':1,'4':2,'5':1,'6':1,'7':1,'8':1,'9':1}
uppper1={'0':2,'1':0,'2':0,'3':0,'4':2,'5':1,'6':1,'7':0,'8':2,'9':2}
middle={'0':2,'1':0,'2':1,'3':1,'4':1,'5':1,'6':1,'7':0,'8':1,'9':1}
lower={'0':2,'1':0,'2':1,'3':0,'4':0,'5':0,'6':2,'7':0,'8':2,'9':0}
lower1={'0':1,'1':0,'2':1,'3':1,'4':0,'5':1,'6':1,'7':0,'8':1,'9':1}
f=0
e=0
input2=[]
counter=0
while(f==0):
    input1=list(input())
    if(input1[0]=='e'):
        break
    input2.append(input1)
c=0
while(e<=len(input2)-1):
    counter=counter+1
    time=input2[c]
    time.remove(time[2])
    t=0
    count=0
    for i in range(4):
        a=time[t]
        x=uppper[a]
        count=count+1
        if(count==2):
            print(type1[x],end="     ")
            count=count+1
        else:
            print(type1[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for j in range(4):
        a=time[t]
        x=uppper1[a]
        count=count+1
        if(count==2):
            print(type2[x],end="     ")
            count=count+1
        else:
            print(type2[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for j in range(4):
        a=time[t]
        x=uppper1[a]
        count=count+1
        if(count==2):
            print(type2[x],end="  o  ")
            count=count+1
        else:
            print(type2[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for k in range(4):
        a=time[t]
        x=middle[a]
        count=count+1
        if(count==2):
            print(type1[x],end="     ")
            count=count+1
        else:
            print(type1[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for l in range(4):
        a=time[t]
        x=lower[a]
        count=count+1
        if(count==2):
            print(type2[x],end="  o  ")
            count=count+1
        else:
            print(type2[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for l in range(4):
        a=time[t]
        x=lower[a]
        count=count+1
        if(count==2):
            print(type2[x],end="     ")
            count=count+1
        else:
            print(type2[x],end="  ")
        t=t+1
    print()
    t=0
    count=0
    for m in range(4):
        a=time[t]
        x=lower1[a]
        count=count+1
        if(count==2):
            print(type1[x],end="     ")
            count=count+1
        else:
            print(type1[x],end="  ")
        t=t+1   
    print()
    print()
    print()
    e=e+1
    c=c+1
    if(counter==len(input2)):
        print('end')
