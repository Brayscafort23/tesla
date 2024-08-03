import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ejemplo (reemplaza con la URL correcta)
url = 'https://example.com/tesla-revenue'  # Sustituye con la URL correcta

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas las tablas en el HTML
tables = soup.find_all('table')

# Verificar el contenido de cada tabla
for i, table in enumerate(tables):
    print(f'Tabla {i}:')
    print(table.prettify())  # Imprimir el HTML de cada tabla

# Seleccionar y extraer los datos de la tabla correcta (ajustar el índice si es necesario)
if tables:
    tesla_revenue = pd.read_html(str(tables[0]))[0]  # Ajusta el índice de la tabla si es necesario
    print(tesla_revenue.tail())
else:
    print('No se encontraron tablas en la página.')
