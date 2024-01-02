# import libraries
from utilities.utils import Myutils
import datetime as dt
import pandas as pd

# bakery management system
class BakeryManagementSystem:
    # constructor
    def __init__(self) -> None:
        self.orderdata_folder = "./order_data"
        self.orderid_file = "./order_data/orders_id.csv"
        self.orderid = []
        self.cst_name = []
        self.item = []
        self.qty = []
        self.date = []
    
    # function to add order
    def add_order(self):
        customer_name = input("Enter customer name : ")
        bakery_item = input("Enter item to order : ")
        item_qty = int(input("Enter item quantity : "))
        order_date = pd.to_datetime(dt.datetime.today().date())
        # generate order id
        orderid_df = pd.read_csv(self.orderid_file)
        first_row, first_value = Myutils.get_index_and_value(orderid_df, "first")
        if first_value != 0:
            last_row, last_value = Myutils.get_index_and_value(orderid_df, "last")
            current_orderid = int(last_value + 1)
            current_order_row = last_row + 1
        else:
            current_order_row = first_row
            current_orderid = int(first_value + 1)
        
        # create data-frame
        self.orderid.append(current_orderid)
        self.cst_name.append(customer_name)
        self.item.append(bakery_item)
        self.qty.append(item_qty)
        self.date.append(order_date)
        
        order_dict = {
            "Order_Id" : self.orderid,
            "Customer_Name" : self.cst_name,
            "Item" : self.item,
            "Quantity" : self.qty,
            "Date" : self.date
        }
        order_df = pd.DataFrame(order_dict)
        order_df.to_csv(self.orderdata_folder + "/" + str(current_orderid) + ".csv", index = False)  
        
        # update order_id data
        Myutils.update_orderid_file(current_order_row, current_orderid)
        
        # print order id
        print()
        print(order_df.head(), "\n")
        print("Order placed successfully")
        print(f"Your order id is {current_orderid}", "\n")
    
    # function to view order
    def view_order(self):
        orderid = int(input("Enter order id : "))
        df = pd.read_csv(self.orderdata_folder + "/" + str(orderid) + ".csv")
        print(df.head(), "\n")
        
    # function to update exsiting order
    def update_order(self):
        # print existing order
        orderid = int(input("Enter order id : "))
        df = pd.read_csv(self.orderdata_folder + "/" + str(orderid) + ".csv")
        row_idx = Myutils.get_last_index(df, "Order_Id")
        
        print(df.head(), "\n")
        print("Enter 1 to update item")
        print("Enter 2 to update quantity")
        print("Enter 3 to update item and quantity")
        print("Enter 4 to add new item", "\n")
        
        option = int(input("Enter your choice : "))
        if option == 1:
            updated_item = input("Enter new item : ")
            df.loc[row_idx,"Item"] = updated_item
            df.to_csv(self.orderdata_folder + "/" + str(orderid) + ".csv", index = False)
            print(df.head(), "\n")
            print("Your order updated successfully")
        elif option == 2:
            updated_qty = int(input("Enter new quantity : "))
            df.loc[row_idx,"Quantity"] = updated_qty
            df.to_csv(self.orderdata_folder + "/" + str(orderid) + ".csv", index = False)
            print(df.head(), "\n")
            print("Your order updated successfully")
        elif option == 3:
            updated_item = input("Enter new item : ")
            updated_qty = int(input("Enter new quantity : "))
            df.loc[row_idx,"Item"] = updated_item; df.loc[row_idx,"Quantity"] = updated_qty
            df.to_csv(self.orderdata_folder + "/" + str(orderid) + ".csv", index = False)
            print(df.head(), "\n")
            print("Your order updated successfully")
        elif option == 4:
            new_item = input("Enter new item : ")
            new_qty = int(input("Enter new quantity : "))
            # update data
            df = pd.read_csv("./order_data" + "/" + str(orderid) + ".csv")
            row_idx = Myutils.get_last_index(df, "Order_Id")
            df.loc[row_idx + 1, "Item"] = new_item
            df.loc[row_idx + 1, "Quantity"] = new_qty
            df.to_csv(self.orderdata_folder + "/" + str(orderid) + ".csv", index = False)
            print(df.head(), "\n")
            print("New item added successfully")
    