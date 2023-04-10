class Item:
    def __init__(self, name,  price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# GUIDE: kalo mau nambah item nama item huruf kecil semua
item_1 = Item("pensil", 20000, 100)
item_2 = Item("pulpen", 1000, 122)
item_3 = Item("buku", 30000, 121)
item_4 = Item("tas", 100000, 291)
item_5 = Item("kertas", 1000, 500)

Shop = [item_1, item_2, item_3, item_4, item_5]

def display_item():
    print("|\t" + "NAMA   " + "\t|\t" + "HARGA     " + "\t|   " + "TOTAL STOK" + "\t|")
    print("---------------------------------------------------------")
    for item in Shop:
        print("|\t" + item.name.capitalize() + "\t|\t" + "Rp.{:,}".format(item.price) + "\t|\t" + str(item.stock) + "\t|")

def totalPrice(cart):
    total = 0
    for price in cart:
        total = total + price["price"]
    return total

def Payment_Program():
    print("\n")
    print("\n")

    cart = []

    print("-------------------- Payment Program --------------------")
    display_item()
    print("---------------------------------------------------------")

    while True:
        item = input("What would you like to buy: (or 'done' to finish): ")

        if item.lower() == 'done':
            break

        item_track = False

        for items in Shop:
            if item.lower() == items.name:
                item_track = not item_track

        if item_track == False:
            print("\nInvalid item name, please enter a valid item name!\n")
        else:
            quantity = int(input("Enter the quantity: "))
            for items in Shop:
                if items.name == item:
                    while quantity > items.stock:
                        quantity = int(input("Enter the correct amount: "))
                    else:
                        items.stock = items.stock - quantity
                        items_price = quantity * items.price
                        cart.append({"name": item, "stock": quantity, "price": items_price})
                        print("Harga: {:,}".format(items_price) + "\n")
                        display_item()

    print("\nThanks for visiting our store, here's your total purchase: \n")
    print("---------------------------------------------------------")
    print("|\t" + "NAMA" + "\t|\t" + " HARGA  " + "\t|   " + "JUMLAH ITEM" + "\t|")
    print("---------------------------------------------------------")
    for i in cart:
        print("|\t" + i["name"] + "\t|\tRp. {:,}".format(i["price"]) + "\t|\t" + str(i["stock"]) + "\t|")
    print("---------------------------------------------------------")
    
    total_price = totalPrice(cart)
    print("\tTotal Semua:\tRp.{:,}".format(total_price))

    print("\n")
    print("\n")

Payment_Program()