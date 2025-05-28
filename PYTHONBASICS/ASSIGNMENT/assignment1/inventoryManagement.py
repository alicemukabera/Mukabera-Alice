items = [
    { "id": "A001", "name": "hima cement", "quantity": 50000, "price": 36000 },
    { "id": "B002", "name": "tororo cement", "quantity": 20000, "price": 35000 },
    { "id": "C003", "name": "iron sheets", "quantity": 150000, "price": 35000 }
]

def addnewItem():
 items.append({"id":input("enter id"),"name": input("enter name"), "quantity":input("enter quantity"), "price": input("enter price")})
 displayItems()
 return

def displayItems():
      print("Name                        Qty                    Price(ugx)") 
      for item in items: 
    # Convert quantity and price to string before concatenation
          print(item["name"] + "                    " + str(item["quantity"]) + "                      " + str(item["price"]))
          
    
def updateQty():
    itemName = str(input("Enter item Name to be updated "))
    
    for item in items: 
        if itemName.lower() == item['name'].lower():
            print("Name                        Qty                    Price(ugx)") 
            print(item["name"] + "                    " + str(item["quantity"]) + "                      " + str(item["price"]))
            
            Uservalue = int(input("Enter negative quantity in case of purchase and positive in case of restocking\n"))
            item["quantity"] = int(item["quantity"]) + Uservalue
            
            print("UPDATED ITEM\nName                        Qty                    Price(ugx)\n\n\n") 
            print(item["name"] + "                    " + str(item["quantity"]) + "                      " + str(item["price"]))
            break

    displayItems()
    return
        
print('TASKS YOU CAN CARRY OUT\n1.)ADD NEW PRODUCT.\n2.)UPDATE QUANTITY OF A PRODUCT.\n3.)VIEW INVENTORY ITEMS')
option=int(input("SELECT THE TASK YOU WOULD LIKE TO CARRY OUT BY ENTERIING A NUMBER\n"))
if(option==1):
    addnewItem()
elif(option==2):
    updateQty()
else:
    displayItems()
    