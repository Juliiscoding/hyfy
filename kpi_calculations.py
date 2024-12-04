import pandas as pd

def process_excel_data(uploaded_file, sheet_name):
    """Verarbeitet die hochgeladene Excel-Datei und berechnet KPIs."""
    try:
        # Excel-Daten einlesen
        data = pd.read_excel(uploaded_file, sheet_name=sheet_name, skiprows=1)

        # KPI-Berechnungen (Beispiel: Deckungsbeitrag)
        data["Deckungsbeitrag"] = data["Plan_Umsatz_VK"] - data["Plan_Umsatz_EK"]

        return data
    except Exception as e:
        raise ValueError(f"Fehler beim Verarbeiten der Datei: {e}")
