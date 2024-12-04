import streamlit as st
import pandas as pd
from authentication import authenticate_user
from kpi_calculations import process_excel_data

# Logo anzeigen
st.image("images/your_logo.png", use_column_width=True)

# Hauptcode der App beginnt hier
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("You´re all in ONE Retail AI - Solution aus dem Hause Hyperion")
    st.subheader("Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    login_button = st.button("Anmelden")

    if login_button:
        if authenticate_user(username, password):  # Verwende die importierte Funktion
            st.session_state.authenticated = True
            st.success(f"Willkommen, {username}!")
        else:
            st.error("Ungültige Anmeldedaten. Bitte erneut versuchen.")
else:
    st.title("KPI-Dashboard für Limitplanung")
    uploaded_file = st.file_uploader("Laden Sie eine Excel-Datei hoch", type=["xlsx"])

    if uploaded_file:
        sheet_name = st.sidebar.text_input("Sheet-Name eingeben", "Limit")
        data = process_excel_data(uploaded_file, sheet_name)  # Verwende die importierte Funktion
        st.write("Hochgeladene Daten:")
        st.dataframe(data)

