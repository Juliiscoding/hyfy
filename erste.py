import streamlit as st
from authentication import login, logout
from kpi_calculations import upload_and_calculate

# Initialisiere den Authentifizierungsstatus
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()  # Anmeldemaske anzeigen
else:
    upload_and_calculate()  # KPI-Dashboard anzeigen
    logout()  # Abmeldebutton anzeigen
