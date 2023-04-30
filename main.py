import os
import pandas as pd
import gspread
from dotenv import load_dotenv
from google.oauth2 import service_account


load_dotenv()  # Carga las variables de entorno del archivo .env

# set credentials
current_directory = os.path.abspath(os.path.dirname(__file__))
credentials_file_path = os.path.join(current_directory, "credentials.json")
scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = service_account.Credentials.from_service_account_file(credentials_file_path, scopes=scope)


# Autentica y crea una instancia de gspread
gc = gspread.authorize(credentials)
spreadsheet_id = os.environ.get("SPREADSHEET_ID")
sheet = gc.open_by_key(spreadsheet_id)
worksheet = sheet.worksheet("Hoja 1")
data = worksheet.get_all_values()

# Convierte el resultado en un DataFrame de pandas
headers = data.pop(0)  
df = pd.DataFrame(data, columns=headers)
csv_file_path = os.path.join(current_directory, "exercises.csv")
df.to_csv(csv_file_path, index=False)

