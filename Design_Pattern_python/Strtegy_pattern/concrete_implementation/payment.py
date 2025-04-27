# different ways of doing payment
from interface_strategy.payment import PaymentStrtegy


class CreditCardPayment(PaymentStrtegy):

    def pay(self, amount):
        print("amount paid from credit card:", amount)

class PayPal(PaymentStrtegy):

    def pay(self,amount):
        print("amount paid from paypay:", amount)

class PhonePay(PaymentStrtegy):

    def pay(self, amount):
        print("amount paid from phonepay:", amount)
