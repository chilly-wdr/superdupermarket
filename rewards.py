from database import db,cursor,new_id
from datetime import date

def register_customer():
    customer_id=new_id("rewards","customer_id")
    customer_name=input("enter customer name: ")
    mobile_no=int(input("enter customer mobile number: "))
    DOJ=date.today()
    cursor.execute("INSERT INTO REWARDS VALUES(%s,%s,%s,%s,0)",(customer_id,customer_name,mobile_no,DOJ))
    print("customer registered successfully!")
    print("customer id: ",customer_id)
    db.commit()

def update_customer_name():
    customer_id=int(input("enter customer id: "))
    new_name=input("enter new customer name: ")
    cursor.execute("UPDATE REWARDS SET CUSTOMER_NAME=%s WHERE CUSTOMER_ID=%s",(new_name,customer_id))
    print("customer name updated!")
    db.commit()

def update_customer_mobile():
    customer_id=int(input("enter customer id: "))
    new_mobile=int(input("enter new customer mobile number: "))
    cursor.execute("UPDATE REWARDS SET MOBILE_NUMBER=%s WHERE CUSTOMER_ID=%s",(new_mobile,customer_id))
    print("customer mobile number updated!")
    db.commit()

def view_reward_points():
    mobile_no=int(input("enter customer mobile number: "))
    cursor.execute("SELECT REWARD_POINTS FROM REWARDS WHERE MOBILE_NUMBER=%s",(mobile_no,))
    result=cursor.fetchone()
    if result is None:
        print("customer not found")
    else:
        reward_point=result[0]
        print("reward points: ",reward_point)
