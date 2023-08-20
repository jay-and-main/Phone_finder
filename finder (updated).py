import sqlite3
con=sqlite3.connect("somedb.db")
cursor=con.cursor()
sel="select * from Sometable"
row=cursor.execute(sel).fetchall()
#for i in row:
#    print(i)
l_phoneName=[]
for r in row:
    if r[0] not in l_phoneName:
        l_phoneName.append(r[0])

l_compare=[]

def comp_ram(d,d1,x,i,p):
    if p not in d1.values():
        d1["name"]=p
        d1["count"]=1
    elif p in d1.values():
        d1["count"]+=1
    if x[0]==i[1]:
        if p not in d.values():
            d["name"]=p
            d["props"]=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]
            l_compare.append(d)
        elif p in d.values() and d1["count"]<2:
            d["props"]+=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]


 

def comp_sto(d,d2,x,i,p):
    if p not in d2.values():
        d2["name"]=p
        d2["count"]=1
    elif p in d2.values():
        d2["count"]+=1
    if x[1]==i[2]:
        if p not in d.values():
            d["name"]=p
            d["props"]=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]
            l_compare.append(d)
        elif p in d.values() and d2["count"]<2:
            d["props"]+=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]
            

def comp_cost(d,d3,x,i,p):
    if p not in d3.values():
        d3["name"]=p
        d3["count"]=1
    elif p in d3.values():
        d3["count"]+=1
    if x[2]==i[3]:
        if p not in d.values():
            d["name"]=p
            d["props"]=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]
            l_compare.append(d)
        elif p in d.values() and d3["count"]<2:
            d["props"]+=1
            d["ram_count"]=i[1]
            d["sto_count"]=i[2]
            d["cost_range"]=i[3]
            d["cost"]=i[4]
            

    

a=[]
for i in row:
    if i[0]=='IPHONE12':
        a.append(i)
    if i[0]=='ONEPLUSNORD':
        a.append(i)
    



d1={}
d2={}
d3={}
x=[4,64,"10000-20000"]
#y=[4,256,65000]
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
    comp_cost(d,d3,x,i,i[0])
#print(d1)
#print(d2)

def key_max(d):
    return d["props"]
final_l=sorted(l_compare,key=key_max,reverse=True)
for i in range(0,5):
    print("Your",i+1,"preference is:",final_l[i]['name'])
    print("Ram:",final_l[i]['ram_count'])
    print("Storage:",final_l[i]['sto_count'])
    #print("Cost Range:",final_l[i]['cost_range'])
    print("Cost:",final_l[i]['cost'])
'''
for i in range(0,5):
    print(final_l[i])
    if final_l[i]['props']==3:
        item_list=final_l[i].values()
        final_items_list=[]
        for j in item_list:
            final_items_list.append(j)
        print("Ram:",final_items_list[2])
        print("Storage:",final_items_list[3])
        print("Cost Range:",final_items_list[4])
'''        
         