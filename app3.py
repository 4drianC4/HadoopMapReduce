#EL DEBER
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def extract_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Hacer una solicitud a la página web con el User-Agent especificado
    response = requests.get(url, headers=headers)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error: Unable to access page (status code: {response.status_code})")
        return None

    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer texto de la página (puedes ajustar esto según la estructura de la página)
    page_text = soup.get_text(separator='\n', strip=True)

    return page_text

def extract_content_for_date_range(start_date, end_date):
    current_date = start_date
    all_page_text = ""
    
    while current_date <= end_date:
        print(f"Extracting content for {current_date.strftime('%Y-%m-%d')}")
        # Construir la URL para la fecha actual
        url = f"https://eldeber.com.bo/ultimas-noticias/{current_date.day:02d}-{current_date.month:02d}-{current_date.year}/"
        
        # Extraer el contenido de la página y agregarlo al texto total
        page_text = extract_content(url)
        if page_text:
            all_page_text += f"Date: {current_date.strftime('%Y-%m-%d')}\n{page_text}\n\n"
        
        # Moverse a la siguiente fecha
        current_date += timedelta(days=1)
    
    return all_page_text

if __name__ == "__main__":
    # Ingresar la fecha de inicio y la fecha de fin
    start_date_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    end_date_str = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    # Extraer el contenido para el rango de fechas especificado
    all_page_text = extract_content_for_date_range(start_date, end_date)
    
    # Guardar el texto en un archivo de texto plano
    with open('page_content2.txt', 'w', encoding='utf-8') as file:
        file.write(all_page_text)
    
    print("Contenido extraído y guardado en page_content.txt")
