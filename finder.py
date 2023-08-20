import sqlite3
con=sqlite3.connect("somedb.db")
cursor=con.cursor()
sel="select * from Sometable"
row=cursor.execute(sel).fetchall()

l_phoneName=[]
for r in row:
    if r[0] not in l_phoneName:
        l_phoneName.append(r[0])

l_compare=[]

def comp_ram(d,d1,x,i,p):
    if p not in d1:
        d1[p]=1
    elif p in d1:
        d1[p]+=1
    if x[0]==i[1]:
        if p not in d:
            d[p]=1
            l_compare.append(d)
        elif p in d and d1[p]<2:
            d[p]+=1
        
 

def comp_sto(d,d2,x,i,p):
    if p not in d2:
        d2[p]=1
    elif p in d2:
        d2[p]+=1
    if x[1]==i[2]:
        if p not in d:
            d[p]=1
            l_compare.append(d)
        elif p in d and d2[p]<2:
            for i in l_compare:
                if p in i:
                    d[p]+=1
            

def comp_cost(d,d3,x,i,p):
    if p not in d3:
        d3[p]=1
    d3[p]+=1
    if x[2]==i[3]:
        if p not in d:
            d[p]=1
            l_compare.append(d)
        elif p in d and d3[p]<2:
            d[p]+=1
            

    

a=[]
for i in row:
    if i[0]=='IPHONE12':
        a.append(i)
    if i[0]=='ONEPLUSNORD':
        a.append(i)
    



d1={}
d2={}
d2={}
x=[4,128,23000]
y=[4,256,65000]
#a.pop(2)
#print(a)
#comp_ram(d,d1,x,a[0],a[0][0])
#comp_ram(d,d1,x,a[1],a[1][0])
#comp_ram(d,d1,x,a[2],a[2][0])
#comp_ram(d,d1,y,a[0],a[0][0])
#comp_ram(d,d1,y,a[1],a[1][0])
#comp_ram(d,d1,y,a[2],a[2][0])
#comp_sto(d,d2,x,a[0],a[0][0])
#comp_sto(d,d2,x,a[1],a[1][0])
#omp_sto(d,d2,x,a[2],a[2][0])
d={}
for i in row:
    for j in l_compare:
        if i[0] not in j:
            d={}
    comp_ram(d,d1,x,i,i[0])
    comp_sto(d,d2,x,i,i[0])
#print(d1)
#print(d2)

print(l_compare)

key_max=zip(l_compare.values(),l_compare.keys())

 

