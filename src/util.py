from enum import Enum

class Gain_Type(Enum):
    SHORT = 1
    LONG = 2
    ORIDINARY = 3
    
    def __str__(self):
        if self == Gain_Type.SHORT:
            return "Short"
        elif self == Gain_Type.LONG:
            return "Long"
        elif self == Gain_Type.ORIDINARY:
            return "Oridinary"

def orginize_stock_name(stock_name):
    stock_name = stock_name.replace(",", "")
    stock_name = stock_name.replace("=", "")
    stock_name = stock_name.replace("\"", "")
    stock_name = stock_name.replace(" ", "")
    stock_name = stock_name.replace(".", "")
    return stock_name.lower()