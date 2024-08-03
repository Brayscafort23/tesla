import requests
from bs4 import BeautifulSoup

# URL de ejemplo (reemplaza con la URL correcta)
url = 'https://example.com/tesla-revenue'  # Sustituye con la URL correcta

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Imprimir el contenido HTML para depuración
print(soup.prettify())
