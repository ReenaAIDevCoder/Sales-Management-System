from datetime import datetime


def format_currency(value):

    if value is None:
        value = 0

    return f"₹{value:,.2f}"


def format_date(value):

    if not value:
        return ""

    if isinstance(value, datetime):
        return value.strftime("%d %b %Y")

    return value.strftime("%d %b %Y")


def calculate_percentage(value, total):

    if not total:
        return 0

    return round(
        (value / total) * 100,
        2
    )