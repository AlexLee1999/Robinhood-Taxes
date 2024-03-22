import pandas
from datetime import datetime
import src.table
import src.wash_sales_transactions
import src.transactions
import src.util

class Parser:
    def __init__(self, file_path, output_path):
        self._file_path = file_path
        self._output_path = output_path
        self._table = src.table.Table()
        
    def parsing(self):
        df = pandas.read_csv(self._file_path)
        num_rows = len(df)
        total_gain = 0.0
        total_cost = 0.0
        total_proceeds = 0.0
        total_wash_sale_disallowed = 0.0
        for i in range(num_rows - 1):
            original_name = df["Description"][i][2:-1].replace(',', '')
            name = src.util.orginize_stock_name(original_name)
            open_date = datetime.strptime(df["Open Date"][i], "=\"%m/%d/%Y\"").date().strftime("%m/%d/%Y")
            closed_date = datetime.strptime(df["Closed Date"][i], "=\"%m/%d/%Y\"").date().strftime("%m/%d/%Y")
            event = df["Event"][i][2:-1]
            short_term_gain = df["ST G/L"][i][2:-1].replace('$', '').replace(',', '')
            total_gain += float(short_term_gain)
            long_term_gain = df["LT G/L"][i][2:-1].replace('$', '').replace(',', '')
            gain_type = src.util.Gain_Type.LONG
            delta = datetime.strptime(df["Closed Date"][i], "=\"%m/%d/%Y\"") - datetime.strptime(df["Open Date"][i], "=\"%m/%d/%Y\"")
            gain = 0.0
            if abs(delta.days) > 365:
                gain_type = src.util.Gain_Type.LONG
                gain = long_term_gain
            else:
                gain_type = src.util.Gain_Type.SHORT
                gain = short_term_gain
            cost = df["Cost"][i][2:-1].replace('$', '').replace(',', '')
            proceeds = df["Proceeds"][i][2:-1].replace('$', '').replace(',', '')
            quantity = df["Qty"][i][2:-1]
            
            if event == "Wash":
                key = f"{name}-{closed_date}"
                new_wash_sales_transactions = src.wash_sales_transactions.Wash_Sales_Transactions(
                    name=name,
                    original_name=original_name,
                    acquired_date=open_date,
                    sold_date=closed_date,
                    cost=float(cost),
                    proceeds=float(proceeds),
                    gain_type=gain_type,
                    quantity=float(quantity),
                    gain=float(gain)
                )
                self._table.add_wash_sales_transactions(new_wash_sales_transactions, key)
                total_wash_sale_disallowed += float(gain)
            else:
                new_transactions = src.transactions.Transactions(
                    name=name,
                    original_name=original_name,
                    acquired_date=open_date,
                    sold_date=closed_date,
                    cost=float(cost),
                    proceeds=float(proceeds),
                    is_wash_sale=False,
                    gain_type=gain_type,
                    quantity=float(quantity),
                    gain=float(gain),
                    code="",
                    wash_sale_disallowed=0.0
                )
                self._table.add_transactions(new_transactions)
                total_proceeds += float(proceeds)
                total_cost += float(cost)
        print(f"Total Proceeds: {total_proceeds}, Total Cost: {total_cost}, Total Gain: {total_gain}, Total Wash Sale Disallowed: {total_wash_sale_disallowed}")
    
    def merging_same_day_transactions(self):
        self._table.merge_transactions()
        self._table.merged_wash_sales_transactions()
    
    def mark_wash_sales(self):
        for wash in self._table._merged_wash_sales:
            self._table.mark_wash_sales(wash)
    
    def calculate_total_gain(self):
        total_gain = 0.0
        total_cost = 0.0
        total_proceeds = 0.0
        total_wash_sale_disallowed = 0.0
        for trans in self._table._transactions:
            total_cost += trans._cost
            total_proceeds += trans._proceeds
            total_gain += trans._gain
            total_gain += trans._wash_sale_disallowed
            total_wash_sale_disallowed += trans._wash_sale_disallowed
        print(f"Total Proceeds: {total_proceeds}, Total Cost: {total_cost}, Total Gain: {total_gain}, Total Wash Sale Disallowed: {total_wash_sale_disallowed}")
    
    def calculate_total_gain_in_integer(self):
        total_gain = 0
        total_cost = 0
        total_proceeds = 0
        total_wash_sale_disallowed = 0
        for trans in self._table._transactions:
            total_cost += round(trans._cost)
            total_proceeds += round(trans._proceeds)
            total_gain += round(trans._gain)
            total_gain += round(trans._wash_sale_disallowed)
            total_wash_sale_disallowed += round(trans._wash_sale_disallowed)
        print(f"Total Proceeds: {total_proceeds}, Total Cost: {total_cost}, Total Gain: {total_gain}, Total Wash Sale Disallowed: {total_wash_sale_disallowed}")
    
    def output_csv(self):
        count = 1
        with open(self._output_path, "w") as file:
            file.write(", Name, Original Name, Acquired Date, Sold Date, Proceeds, Cost, Is Wash Sale, Gain Type, Quantity, Gain, Code, Wash Sales Disallowed\n")
            for trans in self._table._transactions:
                file.write(f"{count}, ")
                file.write(trans.to_csv())
                count += 1