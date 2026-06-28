import mysql.connector as m
db=m.connect(host='localhost',user='root',passwd='tuple',database='supermarket')

cursor=db.cursor()

def new_id(table,column):
    cursor.execute("SELECT MAX(%s) FROM %s",(column,table))
    max_id_tup=cursor.fetchone()
    if max_id_tup[0]==None:
        max_id=101
    else:
        max_id = max_id_tup[0] + 1

