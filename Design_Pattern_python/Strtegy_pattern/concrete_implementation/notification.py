from interface_strategy.notification import NotificationStrategy


class EmailNotification(NotificationStrategy):

    def notify(self, message):
        print("Notified by email:", message)


class SMSNotification(NotificationStrategy):

    def notify(self, message):
        print("Notified by sms:", message)

class PushNotification(NotificationStrategy):

    def notify(self, message):
        print("notified by push:", message)

