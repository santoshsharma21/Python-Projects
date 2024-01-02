# import libraries
import pandas as pd 
import datetime as dt

class Myutils:
    # method returns first index and value
    @staticmethod
    def get_index_and_value(data_frame, value_type:str):
        index = 0; value = 0;
        col = data_frame.columns[0]
        if value_type == "first":
            value = data_frame[col][0]
            index = data_frame[data_frame[col] == value].index[0]
        elif value_type == "last":
            value = data_frame[col].iloc[-1]
            index = data_frame[data_frame[col] == value].index[0]
        return index, value
    
    # method will update file
    @staticmethod
    def update_orderid_file(index:int, current_orderid:int):
        data_frame = pd.read_csv("./order_data/orders_id.csv")
        data_frame.loc[index,"last_order_id"] = current_orderid
        data_frame.loc[index, "date"] = pd.to_datetime(dt.datetime.today().date())
        data_frame.to_csv("./order_data/orders_id.csv", index=False)
    
    # returns row value from order data
    def get_last_index(data_frame, col:str) -> int:
         return data_frame[col].index[-1]