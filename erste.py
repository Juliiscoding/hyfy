import streamlit as st

# CSS für zentriertes Layout und responsives Design
st.markdown(
    """
    <style>
    /* Gesamtes Layout zentrieren */
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
        margin: 0;
    }

    /* Logo anpassen */
    .logo-container img {
        max-width: 60%; /* Passt das Logo flexibel an */
        height: auto;
        margin-bottom: 20px;
    }

    /* Login-Formular zentrieren */
    .login-container {
        text-align: center;
        width: 100%;
        max-width: 400px; /* Maximale Breite für die Anmeldemaske */
    }

    /* Login-Button Design */
    button[kind="primary"] {
        background-color: #007BFF; /* Ändert die Farbe des Buttons */
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    button[kind="primary"]:hover {
        background-color: #0056b3;
    }

    /* Text-Styling für den Titel */
    h2 {
        text-align: center;
        font-family: "Avenir", Arial, sans-serif; /* Avenir mit Fallbacks */
        font-size: 24px; /* Schriftgröße anpassen */
        font-weight: 400; /* Schriftstärke */
        color: #333; /* Farbe des Titels */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from authentication import authenticate_user
from kpi_calculations import process_excel_data

# Initialisiere den Authentifizierungsstatus
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

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
            st.session_state.authenticated = True
            st.success(f"Willkommen, {username}!")
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")
else:
    # KPI-Dashboard
    st.title("KPI-Dashboard für Limitplanung")

    # Excel-Datei hochladen
    uploaded_file = st.file_uploader("Laden Sie eine Excel-Datei hoch", type=["xlsx"])
    if uploaded_file:
        sheet_name = st.sidebar.text_input("Sheet-Name eingeben", "Limit")
        try:
            data = process_excel_data(uploaded_file, sheet_name)  # Funktion aus kpi_calculations.py
            st.write("Hochgeladene Daten:")
            st.dataframe(data)
        except Exception as e:
            st.error(f"Fehler beim Verarbeiten der Datei: {e}")
