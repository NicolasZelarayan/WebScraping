from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL de la página web que deseas analizar
url = 'https://play.livetables.io/roulette/?game_id=7&table_id=5001&limit_id=764589&identifier=1010800145ae9c56da939ea17ad681d181ecb8a7'

# Hacer una solicitud GET a la página web
page = requests.get(url)

# Crear un objeto BeautifulSoup para analizar el contenido HTML de la página
soup = BeautifulSoup(page.content, 'html.parser')

# Supongamos que deseas encontrar todos los números en la página. Reemplaza 'tag_name' con la etiqueta HTML real de los números.
numbers = soup.find_all('tag_name')

# Crear una lista para almacenar los resultados
results = []

# Extraer el texto de cada número y agregarlo a la lista de resultados
for number in numbers:
    results.append(number.text)

# Crear un DataFrame usando pandas con la lista de resultados
df = pd.DataFrame({'Numbers': results})

# Escribir el DataFrame en un archivo Excel llamado 'output.xlsx' sin incluir índices
df.to_excel('output.xlsx', index=False)

# Imprimir los resultados y el código de estado HTTP de la solicitud
print(results)
print(page.status_code)
