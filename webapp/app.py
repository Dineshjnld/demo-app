import streamlit as st
from PIL import Image
from pathlib import Path

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

def write_header():
    """Writes the header part of the UI.
    """
    st.title(':blue[AI Based IT Training System]')

def write_footer():
    """Writes the footer part of the UI.
    """
    
    st.sidebar.warning(':blue[Please note that this tool is only for demo purpose]')
    st.sidebar.image("webapp/static/imgs/logo.png", use_column_width=True)
    st.sidebar.warning(':blue[AI Based Training System]')

def write_ui():
    """Handles the major part of the UI.
    """
    if "demo_started" not in st.session_state:
        # Display the login page if the user has not logged in
        write_login_page()
    else:
        # User has logged in, display the rest of the UI
        if "viva_mode" in st.session_state:
            display_course_banner(st.session_state["course_selected"])
            st.markdown("---")
            display_viva_chat_bot(st.session_state["course_selected"])
        elif "video_selected" not in st.session_state:
            display_course_banner(st.session_state["course_selected"])
            display_video_tabs(st.session_state["course_selected"])
        else:
            st.markdown("---")
            video_selected = st.session_state["video_selected"]
            display_video_content(Path(video_selected))
            display_qa_chat_bot()

def production_mode():
    hide_streamlit_style = """
    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    a[class^="viewerBadge_container*"]  {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == '__main__':
    # Provide the direct path to your image file
    img_path = 'webapp/static/imgs/logo.png'
    
    # Check if the image file exists before attempting to open it
    if Path(img_path).is_file():
        img = Image.open(img_path)
    else:
        st.error(f"Image file not found at '{img_path}'")
        img = None

    st.set_page_config(
        page_title='AI Learning Catalysts',
        page_icon=img,
        layout='wide')

    write_header()
    write_ui()
    write_footer()
