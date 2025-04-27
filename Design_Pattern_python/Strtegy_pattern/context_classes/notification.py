from interface_strategy.notification import NotificationStrategy


class NotificationContext:

    def __init__(self, notification: NotificationStrategy):
        self.notification_system = notification

    def set_notification_system(self, notification_strategy: NotificationStrategy):
        self.notification_system = notification_strategy

    def notify(self, message):
        self.notification_system.send_notification(
            message
        )