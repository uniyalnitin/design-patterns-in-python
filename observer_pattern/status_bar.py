from .stock_observer import StockObserver
from .stock import Stock


class StatusBarObserver(StockObserver):

    def __init__(self) -> None:
        self.stocks = []
    
    def add_stocks(self, stock):
        self.stocks.append(stock)
        stock.add_observer(self)

    def show(self):
        for stock in self.stocks:
            print(stock.symbol, stock.get_price())
        print()

    def update(self):
        self.show()