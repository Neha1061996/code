from interface_strategy.notification import NotificationStrategy


class EmailNotification(NotificationStrategy):

    def send_notification(self, message):
        print("Notified by email:", message)


class SMSNotification(NotificationStrategy):

    def send_notification(self, message):
        print("Notified by sms:", message)

class PushNotification(NotificationStrategy):

    def send_notification(self, message):
        print("notified by push:", message)

