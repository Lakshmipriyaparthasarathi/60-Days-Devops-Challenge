import os

username = os.getenv("USER", "default_user")
print(f"Current user: {username}")
