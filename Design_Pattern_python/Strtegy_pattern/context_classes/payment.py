from interface_strategy.payment import PaymentStrtegy


class PaymentContect:

    def __init__(self, strategy: PaymentStrtegy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

    def set_strategy(self, strategy:PaymentStrtegy):
        self.strategy = strategy