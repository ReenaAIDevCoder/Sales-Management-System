import re


def is_valid_email(email):

    if not email:
        return False

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(pattern, email) is not None


def is_valid_phone(phone):

    if not phone:
        return False

    cleaned_phone = re.sub(
        r"[\s\-\(\)]",
        "",
        phone
    )

    return cleaned_phone.isdigit() and len(cleaned_phone) >= 10


def is_required(value):

    return bool(
        value and str(value).strip()
    )