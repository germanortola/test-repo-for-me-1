import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("password")

def password_printer():
     print(f"My password is {password.upper()}")

password_printer()
