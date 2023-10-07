import streamlit as st

# Define a dictionary of valid usernames and passwords (you should replace these with your actual credentials)
valid_credentials = {"user": "training"}

def write_login_page():
    """Displays a login page with username and password input fields.
    """
    st.title(':red[Login]')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_credentials(username, password):
            st.session_state["demo_started"] = True
            # Reload the page to update the session state
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def validate_credentials(username, password):
    """Validates the entered username and password.
    """
    return valid_credentials.get(username) == password

def display_courses():
    """Displays a list of available courses to the user.
    """
    st.title("Available Courses")
    st.write("Course 1: Introduction to AI")
    st.write("Course 2: Machine Learning Fundamentals")
    st.write("Course 3: Deep Learning Essentials")
    # Add more courses as needed

def write_ui():
    """Handles the major part of the UI.
    """
    if "demo_started" not in st.session_state:
        # Display the login page if the user has not logged in
        write_login_page()
    else:
        # User has logged in, display the courses or course information
        display_courses()  # Display available courses

if __name__ == '__main__':
    st.set_page_config(
        page_title='AI Learning Catalysts',
        layout='wide')

    write_ui()
