from .stock import Stock
from .status_bar import StatusBarObserver
from .stock_list_view import StockListObserver

def main():
    stock = Stock("APPL", 200)
    status_bar_observer = StatusBarObserver()
    status_bar_observer.add_stocks(stock)
    stock_list_observer = StockListObserver(stock)
    stock.set_price(300)

    stock_2 = Stock("BPCL", 200)
    status_bar_observer.add_stocks(stock_2)

    stock_2.set_price(300)
    stock_2.set_price(400)
    stock.set_price(500)

main()

## running instruction `python3 -m observer_pattern.entrypoint`