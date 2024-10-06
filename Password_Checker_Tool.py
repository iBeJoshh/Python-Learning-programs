import re

# List of common weak passwords to avoid
common_passwords = ["password", "123456", "qwerty", "password123", "admin", "letmein", "welcome"]

# Function to check for sequential characters (e.g., "abc", "123")
def is_sequential(password):
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
            return True
    return False

# Function to check for repeated characters (e.g., "aaaaaa")
def has_repeated_characters(password):
    return any(password.count(char) > 3 for char in set(password))

def check_password_strength(password):
    strength = {
        "length": len(password) >= 12,  # Increased minimum length
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'[0-9]', password)),
        "symbols": bool(re.search(r'[@$!%*#?&]', password)),
        "not_common": password.lower() not in common_passwords,
        "not_sequential": not is_sequential(password),
        "no_repeats": not has_repeated_characters(password)
    }

    score = sum(strength.values())

    if score == 8:
        return "Very Strong password!"
    elif 6 <= score < 8:
        return "Strong password!"
    elif 4 <= score < 6:
        return "Moderate password. Try adding more variety."
    else:
        return "Weak password. Consider making it longer and more complex."

def suggest_improvements(password):
    suggestions = []
    if len(password) < 12:
        suggestions.append("Increase the length to at least 12 characters.")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        suggestions.append("Add at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one number.")
    if not re.search(r'[@$!%*#?&]', password):
        suggestions.append("Add at least one special character (e.g., @, $, !, %, etc.).")
    if password.lower() in common_passwords:
        suggestions.append("Avoid using common passwords.")
    if is_sequential(password):
        suggestions.append("Avoid sequential characters (e.g., 'abc', '123').")
    if has_repeated_characters(password):
        suggestions.append("Avoid using the same character repeatedly.")

    return suggestions

# Loop until a strong password is provided
while True:
    password = input("Enter your password: ")

    # Check password strength
    result = check_password_strength(password)
    print(result)

    # If the password is very strong or strong, break out of the loop
    if "Strong" in result:
        break

    # Provide suggestions if needed
    improvements = suggest_improvements(password)
    for suggestion in improvements:
        print(f"- {suggestion}")
    print("Please try again.\n")


#Joshua Adkins
