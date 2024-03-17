

class Transactions:
    def __init__(self, name, original_name, acquired_date, sold_date, proceeds, cost, is_wash_sale, gain_type, quantity, gain, code, wash_sale_disallowed):
        self._name = name
        self._original_name = original_name
        self._acquired_date = acquired_date
        self._sold_date = sold_date
        self._proceeds = proceeds
        self._cost = cost
        self._is_wash_sale = is_wash_sale
        self._gain_type = gain_type
        self._quantity = quantity
        self._gain = gain
        self._code = code
        self._wash_sale_disallowed = wash_sale_disallowed
    
    def mark_wash_sales(self, wash_sale_disallowed):
        self._is_wash_sale = True
        self._code = 'W'
        self._wash_sale_disallowed = wash_sale_disallowed
        
    def __str__(self):
        return f"Name: {self._name}, Original Name: {self._original_name}, Acquired Date: {self._acquired_date}, Sold Date: {self._sold_date}, Proceeds: {self._proceeds}, Cost: {self._cost}, Is Wash Sale: {self._is_wash_sale}, Gain Type: {self._gain_type}, Quantity: {self._quantity}, Gain: {self._gain}, Code: {self._code}, Wash Sale Disallowed: {self._wash_sale_disallowed}\n"

    def to_csv(self):
        return f"{self._name},{self._original_name},{self._acquired_date},{self._sold_date},{self._proceeds:.2f},{self._cost:.2f},{self._is_wash_sale},{self._gain_type},{self._quantity:.2f},{self._gain:.2f},{self._code},{self._wash_sale_disallowed:.2f}\n"