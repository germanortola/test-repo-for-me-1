import os
from dotenv import load_dotenv

password = os.getenv("password")

def password_printer():
    return f"My password is {password}"

