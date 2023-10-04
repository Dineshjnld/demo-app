import streamlit as st

# Define a dictionary of valid usernames and passwords (you should replace these with your actual credentials)
valid_credentials = {"user": "password"}

def main():
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_credentials(username, password):
            st.success("Login Successful!")
            # You can redirect the user to another page or perform other actions here
        else:
            st.error("Invalid username or password")

def validate_credentials(username, password):
    """Validates the entered username and password."""
    return valid_credentials.get(username) == password

if __name__ == '__main__':
    main()
