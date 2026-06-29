from database import db,cursor,new_id
from datetime import date,time,datetime

def no_of_items(bill_id):
    cursor.execute("SELECT COUNT(*) FROM TRANSACTION WHERE BILL_ID=%s",(bill_id,))
    result=cursor.fetchone()
    count=result[0]
    return count

def total_amount(bill_id):
    cursor.execute("SELECT SUM(TOTAL_PRICE) FROM TRANSACTIONS WHERE BILL_ID=%s",(bill_id,))
    result=cursor.fetchone()
    sum=result[0]
    return sum

def customer_reward_points(mobile_no):
    cursor.execute("SELECT REWARD_POINTS FROM REWARDS WHERE MOBILE_NUMBER=%s",(mobile_no,))
    result=cursor.fetchone()
    points=result[0]
    return points

def new_bill(bill_id,staff_id):
    date_of_transaction=date.today().isoformat()
    time_of_transaction=datetime.now().time().replace(microsecond=0)
    no_of_items=no_of_items(bill_id)
    total_amount=total_amount(bill_id)
    reward_customer=input("rewards customer?(Y/N): ")
    mobile_no=int(input("enter customer mobile number: "))
    reward_points=customer_reward_points()
    if reward_customer=='Y':
        if reward_points>100:
            ch=input("Do you want to redeem your points?(Y/N): ")
            if ch=="Y":
                points_redeemed=int(input("enter reward points to redeem: "))
                cursor.execute("UPDATE REWARDS SET REWARD_POINTS=REWARD_POINTS-%s WHERE MOBILE_NUMBER=%s",(points_redeemed,mobile_no))
                total_amount=total_amount-points_redeemed
                cursor.execute("UPDATE REWARDS SET REWARD_POINTS=REWARD_POINTS+%s WHERE MOBILE_NUMBER=%s",(int(total_amount),mobile_no))
            elif ch=='N':
                cursor.execute("UPDATE REWARDS SET REWARD_POINTS=REWARD_POINTS+%s WHERE MOBILE_NUMBER=%s",(int(total_amount),mobile_no))
        cursor.execute("INSERT INTO BILLING VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(bill_id,date_of_transaction,time_of_transaction,staff_id,no_of_items,total_amount,reward_customer,mobile_no,points_redeemed,int(total_amount)))
    elif reward_customer=='N':
        cursor.execute("INSERT INTO BILLING VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(bill_id,date_of_transaction,time_of_transaction,staff_id,no_of_items,total_amount,reward_customer,NULL,NULL,NULL,)) #check what ts null is about
    print("bill created successfully!")

def view_bill():
    bill_id=int(input("enter bill id: "))
    cursor.execute("SELECT * FROM BILLING WHERE BILL_ID=%s",(bill_id,))
    bill=cursor.fetchone()
    print("bill: ",bill)

def view_bills_today():
    date=date.today().isoformat()
    cursor.execute("SELECT * FROM BILLING WHERE DATE_OF_TRANSACTION=%s",(date,))
    result=cursor.fetchall()
    print("bills: ")
    for i in result:
        print(i)
