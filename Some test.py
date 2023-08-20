import csv
import sqlite3



con=sqlite3.connect("somedb.db")
cursor=con.cursor()

drop="drop table if exists Sometable;"
cursor.execute(drop)

table='''CREATE TABLE Sometable(
First Name text not null,
Last Name text,
Questionnare text);'''

cursor.execute(table)

with open("Some test.csv","r") as fh:
    #reader=csv.DictReader(fh)
    reader2=csv.reader(fh)
    r=[]
    for i in reader2:
        r.append([i[1],i[2],i[3]])
    ins="insert into Sometable values(?,?,?)"
    cursor.executemany(ins,r)

sel="select * from Sometable"
row=cursor.execute(sel).fetchall()

for r in row:
    print(r)

con.commit()
