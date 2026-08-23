from datetime import datetime


def create_notification(
    message,
    notification_type="info"
):
    """
    Create a notification dictionary.
    """

    return {
        "message": message,
        "type": notification_type,
        "created_at": datetime.utcnow()
    }


def success_notification(message):
    """
    Create success notification.
    """

    return create_notification(
        message,
        "success"
    )


def warning_notification(message):
    """
    Create warning notification.
    """

    return create_notification(
        message,
        "warning"
    )


def error_notification(message):
    """
    Create error notification.
    """

    return create_notification(
        message,
        "error"
    )