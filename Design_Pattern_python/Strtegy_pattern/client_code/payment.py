from concrete_implementation.payment import CreditCardPayment, PhonePay, PayPal
from context_classes.payment import PaymentContect


def make_payment():
    payment = PaymentContect(CreditCardPayment())
    payment.pay(100)

    payment = PaymentContect(PayPal())
    payment.pay(200)

    payment = PaymentContect(PhonePay())
    payment.pay(200)