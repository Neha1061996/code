from concrete_implementation.notification import EmailNotification, PushNotification, SMSNotification
from context_classes.notification import NotificationContext


def make_notification():
    message = "message"
    NotificationContext(EmailNotification()).notify(message)
    NotificationContext(PushNotification()).notify(message)
    NotificationContext(SMSNotification()).notify(message)