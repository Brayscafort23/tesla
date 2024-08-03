import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ejemplo (reemplaza con la URL correcta)
url = 'https://example.com/tesla-revenue'  # Sustituye con la URL correcta

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar tablas con un selector CSS específico (ajusta el selector según la página)
tables = soup.select('table.data')  # Ajusta el selector según la página

# Verificar y extraer datos
if tables:
    tesla_revenue = pd.read_html(str(tables[0]))[0]
    print(tesla_revenue.tail())
else:
    print('No se encontraron tablas con el selector CSS especificado.')
