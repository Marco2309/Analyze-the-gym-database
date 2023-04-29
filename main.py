import os
import pandas as pd
import gspread
from dotenv import load_dotenv
from google.oauth2 import service_account


load_dotenv()  # Carga las variables de entorno del archivo .env

scope = ["https://www.googleapis.com/auth/spreadsheets"]
current_directory = os.path.abspath(os.path.dirname(__file__))
credentials_file_path = os.path.join(current_directory, "credentials.json")
credentials = service_account.Credentials.from_service_account_file(credentials_file_path, scopes=scope)


# Autentica y crea una instancia de gspread
gc = gspread.authorize(credentials)

# Abre la hoja de cálculo de Google Sheets por ID (puedes encontrar el ID en la URL de la hoja de cálculo)
spreadsheet_id = os.environ.get("SPREADSHEET_ID")
sheet = gc.open_by_key(spreadsheet_id)

# Selecciona la hoja de trabajo en la que estás interesado (puedes cambiar 'Sheet1' al nombre de la hoja que desees)
worksheet = sheet.worksheet("Hoja 1")

# Obtiene todos los valores de la hoja de trabajo
data = worksheet.get_all_values()

# Convierte el resultado en un DataFrame de pandas
headers = data.pop(0)  # Asume que la primera fila contiene los encabezados
df = pd.DataFrame(data, columns=headers)

# Ahora puedes analizar y manipular el DataFrame con pandas
print(df.head())
