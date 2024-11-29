import re

def check_password_strength(password):
    """
    Function to check the strength of a given password.
    :param password: The password string to check.
    :return: A tuple with a boolean and a message indicating validity and feedback.
    """
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    
    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    
    # Check for at least one digit
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    # If all conditions are met, return success
    return True, "Password is strong."

if __name__ == "__main__":
    # Take user input for the password
    password = input("Enter a password to check its strength: ")
    
    # Validate the password and provide feedback
    valid, message = check_password_strength(password)
    if valid:
        print("✅", message)  # Strong password message
    else:
        print("❌", message)  # Weak password feedback

