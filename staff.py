import mysql.connector as m
db=m.connect(host='localhost',user='root',passwd='tuple',database='supermarket')
cursor=db.cursor()

def add_staff():
    n=int(input("how many staff to be added?: "))
    for i in range(n):    
        staff_id=int(input("enter new staff id: "))
        staff_name=input("enter staff name: ")
        mobile_no=int(input("enter staff mobile number: "))
        cursor.execute("INSERT INTO STAFF VALUES({},'{}',{})".format(staff_id,staff_name,mobile_no))
    
def update_staff_name():
    staff_id=int(input("enter staff id: "))
    new_name=input("enter new staff name: ")
    cursor.execute("UPDATE STAFF SET STAFF_NAME='{}' WHERE STAFF_ID={}".format(new_name,staff_id))

def update_staff_mobile():
    staff_id=int(input("enter staff id: "))
    new_mobile=int(input("enter new mobile number: "))
    cursor.execute("UPDATE STAFF SET MOBILE_NUMBER={} WHERE STAFF_ID={}".format(new_mobile,staff_id))

def delete_staff():
    staff_id=int(input("enter staff id: "))
    cursor.execute("DELETE FROM STAFF WHERE STAFF_ID={}".format(staff_id))
