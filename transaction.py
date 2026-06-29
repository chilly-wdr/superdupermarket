from database import db,cursor,new_id
from billing import new_bill

def get_unit_price(prod_id):
    cursor.execute("SELECT PRICE FROM STOCK WHERE PRODUCT_ID=%s",(prod_id,))
    price=cursor.fetchone()
    return price[0]

def calculate_new_stock(prod_id,qty):
    cursor.execute("SELECT STOCK_AVAILABLE-%s FROM STOCK WHERE PRODUCT_ID=%s",(qty,prod_id))
    new_stock=cursor.fetchone()
    cursor.execute("UPDATE STOCK SET STOCK_AVAILABLE=%s WHERE PRODUCT_ID=%s",(new_stock[0],prod_id))
    db.commit()

def new_cart():
    bill_id=new_id("billing","bill_id")
    staff_id=int(input("enter staff id: "))
    while True:
        prod_id=int(input("enter the product id: "))
        qty=int(input("enter the quantity: "))
        calculate_new_stock(prod_id,qty)
        unit_price=get_unit_price(prod_id)
        total_price=unit_price*qty
        cursor.execute("INSERT INTO TRANSACTION VALUES(%s,%s,%s,%s,%s)",(bill_id,prod_id,qty,unit_price,total_price))
        db.commit()
        choice=input("more items?(Y/N): ").upper()
        if choice=='Y':
            continue
        elif choice=='N':
            new_bill(bill_id,staff_id)
            break
        else:
            print("invalid")
    
def view_itemized_bill():
    bill_id=int(input("enter bill id: "))
    cursor.execute("SELECT * FROM TRANSACTION WHERE BILL_ID=%s",(bill_id,))
    result=cursor.fetchall()
    print("bill: ")
    for item in result:
        print(item)



