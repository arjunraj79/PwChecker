import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password is too short"

    # Check for the presence of both lowercase and uppercase characters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Weak: Password must include both lowercase and uppercase letters"

    # Check for numbers
    if not re.search("[0-9]", password):
        return "Weak: Password must include numbers"

    # Check for special characters
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Password must include special characters"

    return "Strong: Password is strong"

# Test the password checker
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(strength)
