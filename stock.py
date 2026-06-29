from database import db,cursor,new_id
from datetime import date

def add_new_product():
    prod_id=new_id("stock","product_id")
    prod_name=input("enter the product name: ")
    stock=int(input("enter stock available: "))
    restock_date=date.today()
    m_price=float(input("enter market price of the product: "))
    price=float(input("enter the price of product: "))
    cursor.execute("INSERT INTO STOCK VALUES(%s,%s,%s,%s,%s,%s)",(prod_id,prod_name,stock,restock_date,m_price,price))
    print("product registered successfully!")
    print("product id: ",prod_id)
    db.commit()

def update_product_name():
    prod_id=int(input("enter the product id: "))
    new_name=input("enter the new product name: ")
    cursor.execute("UPDATE STOCK SET PRODUCT_NAME=%s WHERE PRODUCT_ID=%s",(new_name,prod_id))
    print("product name updated successfully!")
    db.commit()

def update_stock():
    prod_id=int(input("enter the product id: "))
    stock=int(input("enter new stock: "))
    cursor.execute("UPDATE STOCK SET STOCK_AVAILABLE=STOCK_AVAILABLE+%s WHERE PRODUCT_ID=%s",(stock,prod_id))
    print("stock updated successfully!")
    db.commit()

def delete_product():
    prod_id=int(input("enter the product id: "))
    cursor.execute("DELETE FROM STOCK WHERE PRODUCT_ID=%s",(prod_id,))
    print("product deleted successfully!")
    db.commit()

def update_price():
    prod_id=int(input("enter the product id: "))
    new_price=float(input("enter new price for the product: "))
    cursor.execute("UPDATE STOCK SET PRICE=%s WHERE PRODUCT_ID=%s",(new_price,prod_id))
    print("price updated successfully!")
    db.commit()

def update_market_price():
    prod_id=int(input("enter the product id: "))
    new_mprice=float(input("enter new price for the product: "))
    cursor.execute("UPDATE STOCK SET MARKET_PRICE=%s WHERE PRODUCT_ID=%s",(new_mprice,prod_id))
    print("market price updated successfully!")
    db.commit()

def calculate_profit():
    prod_id=int(input("enter the product id: "))
    cursor.execute("SELECT PRICE-MARKET_PRICE FROM STOCK WHERE PRODUCT_ID=%s",(prod_id,))
    profit=cursor.fetchone()
    if profit is None:
        print("product not found")
    else:
        print("profit:", profit)

#def display_product()