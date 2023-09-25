Write a python script to perform CRUD operation on following table of "ESM.db" database.

Employee ( eid, ename, dept, basic, branch). eid must be primary key.

Department : Account, Inventory, IT, HR.

Peform Following Operation.

1. Create table

->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

cur = conn.cursor()

tbl = """create table Employee\
            (\
                eid integer primary key,\
                ename text,\
                dept text,\
                basic integer,\
                branch text\
            );"""

cur.execute(tbl)

conn.commit()

conn.close()

2. Insert 5 Records directly, 5 records using tuple and 5 records using taking input from user
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

cur = conn.cursor()

#record which insert directly are
"""
1|Mitul|Account|45000|Surat
2|Love|IT|75000|Surat
3|Kush|Inventory|50000|Surat
4|Jay|HR|60000|Kadodra
5|Kuldeep|Account|3000|Bardoli
"""

#record insert using tuple
"""
ins = [(6,'Dhruv','HR',50000,'Surat'),
            (7,'Aryan','IT',70000,'Vyara'),
            (8,'Dixit','Inventory',5000,'Vyara'),
            (9,'Kishan','HR',50000,'Rajasthan'),
            (10,'Shivam','Account',20000,'Baroda'),
           ]

cur.executemany("insert into employee values(?,?,?,?,?)",ins)
"""

#record insert  from taking user input
mlis=[]
for i in range(5):
    tlis=[]
    eid = int(input('enter eid :'))
    tlis.append(eid)

    ename = input('enter ename :')
    tlis.append(ename)

    dept = input('enter dept :')
    tlis.append(dept)

    basic = int(input('enter salary :'))
    tlis.append(basic)

    branch = input('enter branch :')
    tlis.append(branch)

    mlis.append(tlis)

cur.executemany("insert into employee values(?,?,?,?,?)",mlis)
conn.commit()

conn.close()

3. Update records who are from "Surat" branch with increment in salary 10%.
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj =  conn.cursor()

query = "update employee\
                    set basic = basic + (basic*10)/100\
                    where branch like 'Surat'"

curobj.execute(query)

conn.commit()

conn.close()

4. Print All records.
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee"

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

5. Print records where dept is "HR" and "IT".
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee\
                where dept like 'HR' or dept like 'IT' "

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

6. Print records in sorting order of department.
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

#ascending order
query = "select * from employee order by dept "

#descending order
"""
query = "select * from employee order by dept "
"""
curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

7. Print records where basic is >6000.
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee\
                where basic>6000 "

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

8. Print records whrere employee name second character is "r".
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee\
                where ename like '_r%' "

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

9. Grouping record of employee who are from "Account" and "Inventory".
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee\
                  group by dept\
                  having dept like 'Account' or dept like 'Inventory'"

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

10. Print all records based on branch name in descending order.
->
from sqlite3 import *

conn = connect('C:\\sqlite\\ESM.db')

curobj = conn.cursor()

query = "select * from employee order by branch desc"

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()
