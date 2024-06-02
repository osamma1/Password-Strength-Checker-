import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 12:
        return "Password is too short, it must be at least 12 characters long."
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not any(char in '!@#$%^&*()-_+=' for char in password):
        return "Password must contain at least one special character (!@#$%^&*()-_+=)."
    
    return "Password is strong."

while True:  # Loop indefinitely
    password = input("Enter your password (press 'q' to quit): ")
    
    if password.lower() == 'q':
        break  # Exit the loop if user enters 'q'
    
    result = check_password_strength(password)
    print(result)


