import streamlit as st
from authentication import authenticate_user
from kpi_calculations import process_excel_data

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
        max-width: 50%; 
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
        font-weight: 400;
        color: #333;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialisiere den Authentifizierungsstatus
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Funktion zur Anzeige der Login-Seite
def show_login_page():
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("images/your_logo.png", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
            st.experimental_set_query_params(page="dashboard")
            st.success(f"Willkommen, {username}!")
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")

# Funktion zur Anzeige des Dashboards
def show_dashboard():
    st.title("KPI-Dashboard für Limitplanung")

    uploaded_file = st.file_uploader("Laden Sie eine Excel-Datei hoch", type=["xlsx"])
    if uploaded_file:
        sheet_name = st.sidebar.text_input("Sheet-Name eingeben", "Limit")
        try:
            data = process_excel_data(uploaded_file, sheet_name)  # Funktion aus kpi_calculations.py
            st.write("Hochgeladene Daten:")
            st.dataframe(data)
        except Exception as e:
            st.error(f"Fehler beim Verarbeiten der Datei: {e}")

    if st.button("Abmelden"):
        st.session_state.authenticated = False
        st.experimental_set_query_params(page="login")

# Hauptlogik zur Navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["login"])[0]

if not st.session_state.authenticated or page == "login":
    show_login_page()
else:
    show_dashboard()
