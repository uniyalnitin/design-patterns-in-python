class Stock:

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.observers = []

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        self.notify_observers()
        
    def add_observer(self, obs):
        self.observers.append(obs)

    def notify_observers(self):
        for obs in self.observers:
            obs.update()