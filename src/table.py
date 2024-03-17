import src.transactions

class Table:
    def __init__(self):
        self._transactions = []
        self._wash_sales_transactions = []
        self._transactions_hash_table = {}
        self._wash_hash_table = {}
        self._merged_wash_sales = []
        
    def add_transactions(self, transactions):
        self._transactions.append(transactions)
    
    def add_wash_sales_transactions(self, wash_sales_transactions, key):
        self._wash_sales_transactions.append(wash_sales_transactions)
        if key not in self._wash_hash_table:
            self._wash_hash_table[key] = []
        self._wash_hash_table[key].append(wash_sales_transactions)

    def merge_transactions(self):
        for key in self._transactions_hash_table:
            name = self._transactions_hash_table[key][0]._name
            original_name = self._transactions_hash_table[key][0]._original_name
            acquired_date = self._transactions_hash_table[key][0]._acquired_date
            sold_date = self._transactions_hash_table[key][0]._sold_date
            proceeds = 0.0
            cost = 0.0
            is_wash_sale = self._transactions_hash_table[key][0]._is_wash_sale
            gain_type = self._transactions_hash_table[key][0]._gain_type
            quantity = 0.0
            gain = 0.0
            code = self._transactions_hash_table[key][0]._code
            wash_sale_disallowed = self._transactions_hash_table[key][0]._wash_sale_disallowed
            for trans in self._transactions_hash_table[key]:
                proceeds += trans._proceeds
                cost += trans._cost
                gain += trans._gain
                quantity += trans._quantity
                
            new_transactions = src.transactions.Transactions(
                    name=name,
                    original_name=original_name,
                    acquired_date=acquired_date,
                    sold_date=sold_date,
                    cost=cost,
                    proceeds=proceeds,
                    is_wash_sale=is_wash_sale,
                    gain_type=gain_type,
                    quantity=quantity,
                    gain=gain,
                    code=code,
                    wash_sale_disallowed=wash_sale_disallowed
                )
            self._merged_transactions.append(new_transactions)
    
    def merged_wash_sales_transactions(self):
        for key in self._wash_hash_table:
            name = self._wash_hash_table[key][0]._name
            original_name = self._wash_hash_table[key][0]._original_name
            acquired_date = self._wash_hash_table[key][0]._acquired_date
            sold_date = self._wash_hash_table[key][0]._sold_date
            proceeds = 0.0
            cost = 0.0
            gain_type = self._wash_hash_table[key][0]._gain_type
            quantity = 0.0
            gain = 0.0
            for trans in self._wash_hash_table[key]:
                proceeds += trans._proceeds
                cost += trans._cost
                gain += trans._gain
                quantity += trans._quantity
            new_wash_sales_transactions = src.wash_sales_transactions.Wash_Sales_Transactions(
                    name=name,
                    original_name=original_name,
                    acquired_date=acquired_date,
                    sold_date=sold_date,
                    cost=cost,
                    proceeds=proceeds,
                    gain_type=gain_type,
                    quantity=quantity,
                    gain=gain
                )
            self._merged_wash_sales.append(new_wash_sales_transactions)

    def mark_wash_sales(self, wash_sales_transactions):
        flag = False
        for trans in self._transactions:
            if trans._name == wash_sales_transactions._name and round(trans._gain, 2) == round(wash_sales_transactions._cost, 2) and abs(wash_sales_transactions._gain) <= abs(trans._gain) and trans._gain < 0 and not trans._is_wash_sale:
                trans.mark_wash_sales(float(wash_sales_transactions._gain))
                flag = True
                break

        if not flag:
            count = 0
            wash_sales_gain = float(wash_sales_transactions._gain)
            for trans in self._transactions:
                if trans._name == wash_sales_transactions._name and trans._sold_date == wash_sales_transactions._sold_date:
                    if round(abs(trans._gain), 2) < round(wash_sales_gain, 2) and wash_sales_gain > 0 and trans._gain < 0:
                        trans.mark_wash_sales(float(abs(trans._gain)))
                        wash_sales_gain -= abs(trans._gain)
                    elif round(abs(trans._gain), 2) >= round(wash_sales_gain, 2) and wash_sales_gain > 0 and trans._gain < 0:
                        trans.mark_wash_sales(wash_sales_gain)
                        flag = True
                        break
        
        if not flag:
            print(wash_sales_transactions)
                    
    def __str__(self):
        table_str = "Transactions:\n"
        for transaction in self._transactions:
            table_str += f"{transaction}"
        return table_str