import mysql.connector as m
db=m.connect(host='localhost',user='root',passwd='tuple',database='supermarket')

cursor=db.cursor(buffered=True)

def new_id(table,column):
    cursor.execute(f"SELECT MAX({column}) FROM {table}")
    max_id_tup=cursor.fetchone()
    if max_id_tup[0] is None:
        max_id=101
    else:
        max_id = max_id_tup[0] + 1
    return max_id
