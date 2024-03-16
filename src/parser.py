import pandas
from datetime import datetime
import src.transactions
import src.table
import src.util


def parsing(file_path):
    new_table = src.table.Table()
    df = pandas.read_csv(file_path)
    num_rows = len(df)
    for i in range(num_rows - 1):
        name = df["Description"][i][2:-1]
        open_date = datetime.strptime(df["Open Date"][i], "=\"%m/%d/%Y\"")
        closed_date = datetime.strptime(df["Closed Date"][i], "=\"%m/%d/%Y\"")
        event = df["Event"][i][2:-1]
        print(event)
        is_wash_sale = True if event == "Wash" else False
        short_term_gain = df["ST G/L"][i][3:-1]
        gain_type = src.util.Gain_Type.LONG
        if short_term_gain != "0.00":
            gain_type = src.util.Gain_Type.SHORT
        cost = df["Cost"][i][2:-1].replace('$', '').replace(',', '')
        proceeds = df["Proceeds"][i][2:-1].replace('$', '').replace(',', '')
        quantity = df["Qty"][i][2:-1]
        new_transactions = src.transactions.Transactions(
            name=name,
            acquired_date=open_date,
            sold_date=closed_date,
            cost=float(cost),
            proceeds=float(proceeds),
            is_wash_sale=is_wash_sale,
            gain_type=gain_type,
            quantity=quantity
        )
        new_table.add_transactions(new_transactions)
    return new_table
        
        