import streamlit as st

USER_CREDENTIALS = {
    "admin": "1234",
    "user1": "password1"
}

def authenticate_user(username, password):  # Funktion umbenannt
    """Prüft, ob Benutzername und Passwort korrekt sind."""
    return USER_CREDENTIALS.get(username) == password

def login():
    """Zeigt die Anmeldemaske an."""
    st.title("You´re all in ONE Retail AI - Solution aus dem Hause Hyperion")
    st.subheader("Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    login_button = st.button("Anmelden")

    if login_button:
        if authenticate_user(username, password):  # Verwendung der umbenannten Funktion
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")

def logout():
    """Zeigt den Abmeldebutton an."""
    if st.button("Abmelden"):
        st.session_state.authenticated = False
        st.experimental_rerun()
