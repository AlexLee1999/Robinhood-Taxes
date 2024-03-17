

class Table:
    def __init__(self):
        self._transactions = []
        self._wash_sales_transactions = []
        
    def add_transactions(self, transactions):
        self._transactions.append(transactions)
    
    def add_wash_sales_transactions(self, wash_sales_transactions):
        self._wash_sales_transactions.append(wash_sales_transactions)
        
    def mark_wash_sales(self, wash_sales_transactions):
        for trans in self._transactions:
            if trans._name == wash_sales_transactions._name and trans._gain == wash_sales_transactions._cost:
                trans.mark_wash_sales(trans._gain * -1)

    def __str__(self):
        table_str = "Transactions:\n"
        for transaction in self._transactions:
            table_str += f"{transaction}"
        return table_str