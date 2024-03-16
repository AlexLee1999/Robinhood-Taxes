class Wash_Sales_Transactions:
    def __init__(self, name, original_name, acquired_date, sold_date, proceeds, cost, gain_type, quantity):
        self._name = name
        self._original_name = original_name
        self._acquired_date = acquired_date
        self._sold_date = sold_date
        self._proceeds = proceeds
        self._cost = cost
        self._gain_type = gain_type
        self._quantity = quantity
    
    def __str__(self):
        return f"Name: {self._name}, Original Name: {self._original_name}, Acquired Date: {self._acquired_date}, Sold Date: {self._sold_date}, Proceeds: {self._proceeds}, Cost: {self._cost}, Gain Type: {self._gain_type}, Quantity: {self._quantity}\n"

    def to_csv(self):
        return f"{self._name},{self._original_name},{self._acquired_date},{self._sold_date},{self._proceeds},{self._cost},{self._gain_type},{self._quantity}\n"