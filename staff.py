from database import db,cursor,new_id

def add_staff():
    n=int(input("how many staff to be added?: "))
    for i in range(n):    
        staff_id=new_id("staff","staff_id")
        staff_name=input("enter staff name: ")
        mobile_no=int(input("enter staff mobile number: "))
        cursor.execute("INSERT INTO STAFF (staff_id, staff_name, mobile_number) VALUES (%s, %s, %s)",
    (staff_id, staff_name, mobile_no))
    print("staff registered successfully!")
    db.commit()

def update_staff_name():
    staff_id=int(input("enter staff id: "))
    new_name=input("enter new staff name: ")
    cursor.execute("UPDATE STAFF SET STAFF_NAME=%s WHERE STAFF_ID=%s",(new_name,staff_id))
    print("staff name updated successfully!")
    db.commit()

def update_staff_mobile():
    staff_id=int(input("enter staff id: "))
    new_mobile=int(input("enter new mobile number: "))
    cursor.execute("UPDATE STAFF SET MOBILE_NUMBER=%s WHERE STAFF_ID=%s",(new_mobile,staff_id))
    print("staff mobile number updated successfully!")
    db.commit()

def delete_staff():
    staff_id=int(input("enter staff id: "))
    cursor.execute("DELETE FROM STAFF WHERE STAFF_ID=%s",(staff_id,))
    print("staff deleted successfully!")
    db.commit()

def display_staff():
    staff_id=int(input("enter the staff id: "))
    cursor.execute("SELECT * FROM STAFF WHERE STAFF_ID=%s",(staff_id,))
    result=cursor.fetchone()
    print(result[0])
    