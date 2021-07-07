def most_frequent():
    string=input("please enter a string: ")
    ci=0
    cs=0
    cp=0
    cm=0
    for i in string:
        if i=='i':
             ci+=1
        elif i=='s':
            cs+=1 
        elif i=='p':
            cp+=1 
        elif i=='m':
            cm+=1 
        else:
            print("enter a string")
    d={}
    d['i']=ci
    d['s']=cs 
    d['p']=cp 
    d['m']=cm
    sort_d = sorted(d.items(),key=lambda x: x[1],reverse=True)
    for j in sort_d:
        print(j[0],"=",j[1])
most_frequent()
