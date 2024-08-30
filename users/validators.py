from django.core.exceptions import ValidationError
import re


def validate_email(value: str) -> None:
    pattern: str = r"^[a-zA-Z0-9_]{2,}@[a-z]{3,10}\.[a-z]{2,10}$"
    if not re.match(pattern, value):
        raise ValidationError("Invalid email address")
