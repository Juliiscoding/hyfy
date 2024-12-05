import streamlit as st

USER_CREDENTIALS = {
    "admin": "1234",
    "user1": "password1"
}

def authenticate_user(username, password):
    """Checks if the username and password are correct."""
    return USER_CREDENTIALS.get(username) == password

def login():
    """Displays the login form."""
    st.title("You´re all in ONE Retail AI - Solution aus dem Hause Hyperion")
    st.subheader("Login")
    
    # Using a form for login to support Enter key submission
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Benutzername")
        password = st.text_input("Passwort", type="password")
        login_button = st.form_submit_button("Anmelden")
        
        if login_button:  # If the login button is clicked or Enter is pressed
            if authenticate_user(username, password):
                st.session_state.authenticated = True
                st.experimental_rerun()  # Reload the app to show the authenticated view
            else:
                st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")

def logout():
    """Displays the logout button."""
    if st.button("Abmelden"):
        st.session_state.authenticated = False
        st.experimental_rerun()

