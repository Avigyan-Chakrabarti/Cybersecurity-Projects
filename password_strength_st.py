import streamlit as st

def check_length(password):
    # Check length
    if len(password) < 6:
        return False
    return True

def is_strong_password(password):
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return False

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return False

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return False

    # Check for special characters
    special_characters = "!@#$%^&*()-_+=<>?/{}[]|"
    if not any(char in special_characters for char in password):
        return False

    # If all checks pass, the password is strong
    return True

def password_strength_indicator(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 25

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 25

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 25

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 25

    return strength

def main():
    st.title("Password Strength Checker")
    password = st.text_input("Enter your password (min 6 characters):", type="password")
    if st.button("Check Password Strength"):
        if not check_length(password):
            st.warning("Sorry!! Password has less than 6 characters.")
        elif is_strong_password(password):
            st.success("Password is strong!")
        else:
            st.warning("Password is weak. Please make sure it meets the criteria.")
            st.text("""
Password strength criteria:
            1) At least 6 characters
            2) At least one uppercase and one lowercase letter
            3) At least one digit
            4) At least one special character
""")
        # Display password strength using progress bar
        strength = password_strength_indicator(password)
        st.progress(strength / 100.0)

if __name__ == "__main__":
    main()
