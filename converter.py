import csv
import sqlite3



con=sqlite3.connect("somedb.db")
cursor=con.cursor()

drop="drop table if exists Sometable;"
cursor.execute(drop)

table='''CREATE TABLE Sometable(PhoneName text not null,
RAM int,
Storage int,
Cost_range text,
Cost int);'''

def normalise(x):
    x1=x.upper().split()
    fx=""
    for i in x1:
        fx+=i
    return fx

def gbless(x):
    y=x.split()
    z=int(y[0])
    return z

def range_check(x):
    if 10000<=int(x)<20000:
        return "10000-20000"
    if 20000<=int(x)<30000:
        return "20000-30000"
    if 30000<=int(x)<40000:
        return "30000-40000"
    if 40000<=int(x)<50000:
        return "40000-50000"
    if 50000<=int(x)<60000:
        return "50000-60000"
    if 60000<=int(x)<70000:
        return "60000-70000"
    if 70000<=int(x)<80000:
        return "70000-80000"
    if 80000<=int(x)<90000:
        return "80000-90000"
    if 90000<=int(x)<100000:
        return "90000-100000"
    

cursor.execute(table)
with open("Responses.csv","r") as fh:
    #reader=csv.DictReader(fh)
    reader2=csv.reader(fh)
    final_list=[]
    for i in reader2:
        fs=normalise(i[1])
        ram_gb=gbless(i[13])
        sto_gb=gbless(i[15])
        cost_range=range_check(i[17])
        final_list.append([fs,ram_gb,sto_gb,cost_range,i[17]])
    #print(final_list)
    ins="insert into Sometable values(?,?,?,?,?)"
    cursor.executemany(ins,final_list)

sel="select * from Sometable"
row=cursor.execute(sel).fetchall()

for r in row:
    print(r)

con.commit()



