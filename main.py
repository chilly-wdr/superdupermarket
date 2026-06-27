cat_choice=1
while True:
    print("""| supermarket manager |
        choose category:
            1. billing
            2. discount
            3. rewards
            4. staff
            5. stock
            6. transactions
            7. back""")
    cat_choice=int(input("enter your choice of category: "))

    if cat_choice==1:
        act_choice=1
        while act_choice!=4:
            print("""| billing | 
                choose action:
                    1. new bill
                    2. search bills
                    3. view bills of the day
                    4. back""")
            act_choice=int(input("enter your choice of action: "))
            #billing.py commands

    elif cat_choice==2:
        act_choice=1
        while act_choice!=4:
            print("""| discount |
                choose action: 
                    1. add new discount
                    2. search discounts
                    3. view current discounts
                    4. back""")
            act_choice=int(input("enter your choice of action: "))
            #discount.py commands

    elif cat_choice==3:
        act_choice=1
        while act_choice!=5:
            print("""| rewards |
                choose action:
                    1. register customer
                    2. update customer name
                    3. update mobile number
                    4. view customer reward points
                    5. back""")
            act_choice=int(input("enter your choice of action: "))
            #rewards.py commands
    
    elif cat_choice==4:
        act_choice=1
        while act_choice!=4:
            print("""| staff |
                choose action:
                    1. add new staff
                    2. update staff name
                    3. update staff mobile number
                    4. back""")
            act_choice=int(input("enter your choice of action: "))
            #staff.py commands

    elif cat_choice==5:
        act_choice=1
        while act_choice!=8:
            print("""| stock |
                choose action:
                    1. add new product
                    2. update product name
                    3. update stock 
                    4. update market price
                    5. update price 
                    6. delete product 
                    7. calculate profit
                    8. back""")
            act_choice=int(input("enter your choice of action: "))
            #stock.py commands

    elif cat_choice==6:
        act_choice=1
        while act_choice!=3:
            print("""| transactions |
                choose action:
                    1. add new transaction
                    2. view transaction
                    3. back""")
            act_choice=int(input("enter your choice of action: "))
            #transactions.py commands
    
    elif cat_choice==7:
        break

    else: 
        print("invalid choice. please choose within the given options.")

print("all done")

            