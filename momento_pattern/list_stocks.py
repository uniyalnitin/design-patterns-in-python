# Momento and iterator pattern"

from datetime import datetime


class Iterator:

    def has_next(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError
    
    def current(self):
        raise NotImplementedError


class Stock:

    def __init__(self, order_id, time, stock_name, type, quantity, price) -> None:
        self.order_id = order_id
        self.stock_name = stock_name
        self.type = type
        self.quantity = quantity
        self.price = price


class CustomerStockList:

    def __init__(self) -> None:
        self.stocks = []
        self.buy_id = None
        self.sell_id = None

    def buy(self, stock):
        self.buy_id = len(self.stocks)
        self.type = "buy"
        self._save_stock(stock)

    def sell(self, stock):
        self.sell_id = len(self.stocks)
        self.type = "sell"
        self._save_stock(stock)
        
    def _save_stock(self, stock):
         self.stocks.append({
            "order_id": stock.order_id, 
            "buy_id": self.buy_id, 
            "sell_id": self.sell_id, 
            "time": datetime.now(),
            "quantity":stock.quantity,
            "price": stock.price
        })
    
    def create_iterator(self):
        return self.ListIterator(self)

    class ListIterator(Iterator):

        def __init__(self, collection):
            self.collection = collection
            self.index = 0
        
        def has_next(self):
            return self.index < len(self.collection.stocks)
        
        def next(self):
            stock = self.collection.stocks[self.index]
            self.index += 1
            return stock
        
        def current(self):
            return self.collection.stocks[self.index]


def main():
    customer_list1 = CustomerStockList()
    stock1 = Stock(1, "11:20", "AAPL", "BUY", 1, 200)
    stock2 = Stock(2, "11:30", "BPCL", "BUY", 2, 300)
    customer_list1.buy(stock1)
    customer_list1.sell(stock1)
    customer_list1.buy(stock2)
    iterator = customer_list1.create_iterator()

    while iterator.has_next():
        print(iterator.next())


main()
