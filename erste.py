import streamlit as st
from authentication import authenticate_user
from kpi_calculations import upload_and_calculate

# CSS for centering and styling
st.markdown(
    """
    <style>
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }
    .logo-container img {
        max-width: 50%;
        height: auto;
        margin-bottom: 20px;
    }
    .login-container {
        text-align: center;
        max-width: 400px;
        margin: auto;
    }
    h2 {
        text-align: center;
        font-family: "Avenir", Arial, sans-serif;
        font-size: 24px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Show login if not authenticated
if not st.session_state.authenticated:
    # Logo
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("images/your_logo.png", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Login form
    st.markdown(
        """
        <div class="login-container">
            <h2>You´re all in ONE Retail AI - Solution aus dem Hause Hyperion</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    login_button = st.button("Anmelden")

    if login_button:
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success("Login erfolgreich!")
            st.experimental_rerun()  # Refresh to reflect the new state
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")
else:
    # Display KPI Dashboard
    upload_and_calculate()
