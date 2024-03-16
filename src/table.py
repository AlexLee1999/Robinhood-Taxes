

class Table:
    def __init__(self):
        self._transactions = []
        self._wash_sales_transactions = []
        
    def add_transactions(self, transactions):
        self._transactions.append(transactions)
    
    def add_wash_sales_transactions(self, wash_sales_transactions):
        self._wash_sales_transactions.append(wash_sales_transactions)
    
    def __str__(self):
        table_str = "Transactions:\n"
        for transaction in self._transactions:
            table_str += f"{transaction}\n"
        return table_str