import pandas as pd
import streamlit as st

def upload_and_calculate():
    """Lädt eine Excel-Datei hoch und berechnet KPIs."""
    st.title("KPI-Dashboard für Limitplanung")

    uploaded_file = st.file_uploader("Laden Sie eine Excel-Datei hoch", type=["xlsx"])
    if uploaded_file:
        sheet_name = st.sidebar.text_input("Sheet-Name eingeben", "Limit")
        data = pd.read_excel(uploaded_file, sheet_name=sheet_name, skiprows=1)
        st.write("Hochgeladene Daten:")
        st.dataframe(data)

        # Beispiel für KPI-Berechnungen
        data["Deckungsbeitrag"] = data["Plan_Umsatz_VK"] - data["Plan_Umsatz_EK"]
        st.write("Berechnete KPIs:")
        st.dataframe(data)
