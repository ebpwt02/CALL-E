import re

def validate_email(email):
    """ Validate the email format. """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")

def validate_phone(phone):
    """ Validate the phone number format. """
    # Example: Simple validation for a 10-digit phone number
    pattern = r'^\d{10}$'
    if not re.match(pattern, phone):
        raise ValueError("Invalid phone number format")

def validate_name(name):
    """ Validate the name. """
    # Example: Check if the name is not empty and does not contain numbers
    if not name or re.search(r'\d', name):
        raise ValueError("Invalid name format")

# Add additional validation functions as needed