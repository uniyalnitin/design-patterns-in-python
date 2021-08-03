from .stock_observer import StockObserver
from .stock import Stock


class StockListObserver(StockObserver):

    def __init__(self,  stock) -> None:
        self.datasource = stock
        self.price = stock.price
        stock.add_observer(self)

    def update(self):
        self.price = self.datasource.get_price()