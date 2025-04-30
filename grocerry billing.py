def grocery_billing():
    print("welcome to the grocerry store:")
    try:
        items=int(input("enter the NO. of items:"))
    except ValueError:
        print("error:enter the correct no.of items")
        return
    products=[]
    total_bill=0
    for i in range(items):
        print(f"\nitem{i+1}:")
        name=input("enter the item name:")
        try:
           price=float(input("enter the price per unit:"))
           quantity=int(input("enter the quantity:"))  
        except ValueError:
           print("error:enter the correct price and auantity") 
           return
        total_price=price * quantity
        products.append((name,price,quantity,total_price))
        total_bill+=total_price
        print("YOUR BILL") 
    for name , price, quantity,total_price in products:
        print(f"{name} - {price} * {quantity} = {total_price}")
        print(f"total amount = {total_bill}")
        print("thank you")

grocery_billing()       

        