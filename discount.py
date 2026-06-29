from database import db,cursor,new_id
from datetime import date

def calculate_discounted_price(prod_id,discount_percent):
    cursor.execute("SELECT PRICE FROM STOCK WHERE PRODUCT_ID=%s",(prod_id,))
    price=cursor.fetchone()
    discounted_price=price[0]-(price[0]*(discount_percent/100))
    return discounted_price

def add_new_discount():
    discount_id=new_id("discount","discount_id")
    prod_id=int(input("enter the product id: "))
    discount_percent=int(input("enter the discount percentage: "))
    discounted_price=calculate_discounted_price(prod_id,discount_percent)
    start_date=input("enter the start date(YYYY-MM-DD): ")
    end_date=input("enter the end date(YYYY-MM-DD): ")
    rewards_only=input("is the discount exclusive for rewards members?(Y/N): ")
    cursor.execute("INSERT INTO DISCOUNT VALUES(%s,%s,%s,%s,%s,%s,%s)",(discount_id,prod_id,discount_percent,discounted_price,start_date,end_date,rewards_only))
    print("discount registered successfully!")
    print("discount id: ",discount_id)
    print("discounted price: ", discounted_price)
    db.commit()

def search_discount():
    discount_id=int(input("enter discount id: "))
    cursor.execute("SELECT * FROM DISCOUNT WHERE DISCOUNT_ID=%s",(discount_id,))
    discount=cursor.fetchone()
    print(discount)

def view_current_discounts():
    cursor.execute("SELECT discount_id,prod_id,discounted_price,end_date FROM DISCOUNT WHERE CURDATE()<=END_DATE")
    result=cursor.fetchall()
    for i in result:
        print(i)

def view_discount_expiry():
    discount_id=int(input("enter discount id: "))
    cursor.execute("SELECT END_DATE FROM DISCOUNT WHERE DISCOUNT_ID=%s",(discount_id,))
    expiry_date=cursor.fetchone()
    print("expiry date: ",expiry_date)

