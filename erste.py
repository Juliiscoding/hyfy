import streamlit as st
from authentication import authenticate_user
from kpi_calculations import upload_and_calculate

# CSS für zentriertes Layout und responsives Design
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
        max-width: 50%; /* Logo passt sich an die Fenstergröße an */
        height: auto;
        margin-bottom: 20px;
    }
    .login-container {
        text-align: center;
        width: 100%;
        max-width: 400px;
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

# Initialisiere den Authentifizierungsstatus
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Authentifizierungs-Logik
if not st.session_state.authenticated:
    # Logo anzeigen
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("images/your_logo.png", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Anmeldemaske
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
        if authenticate_user(username, password):  # Login-Funktion aus authentication.py
            st.session_state.authenticated = True  # Authentifiziert setzen
            st.experimental_set_query_params(authenticated="true")  # Parameter aktualisieren
            st.experimental_rerun()  # App neu laden
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")
else:
    # Zeige das KPI-Dashboard an
    upload_and_calculate()

