from abc import ABC, abstractmethod

class PaymentStrtegy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
