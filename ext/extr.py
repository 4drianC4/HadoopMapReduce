import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def extract_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Unable to access page {url} (status code: {response.status_code})")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text(separator='\n', strip=True)

    return page_text

def get_opinion_url(date):
    return f"https://www.opinion.com.bo/archive/content/{date.year}/{date.month:02d}/{date.day:02d}/"

def get_eldeber_url(date):
    return f"https://eldeber.com.bo/ultimas-noticias/{date.day:02d}-{date.month:02d}-{date.year}/"

def get_lostiempos_url(date):
    date_str = date.strftime("%d/%m/%Y")
    return f"https://www.lostiempos.com/hemeroteca-fecha?fecha={date_str}&seccion=All"

def extract_content_for_date_range(start_date, end_date, newspapers):
    current_date = start_date
    all_page_text = ""
    
    while current_date <= end_date:
        print(f"Extracting content for {current_date.strftime('%Y-%m-%d')}")
        
        for name, get_url in newspapers.items():
            url = get_url(current_date)
            page_text = extract_content(url)
            if page_text:
                all_page_text += f"Newspaper: {name}\nDate: {current_date.strftime('%Y-%m-%d')}\n{page_text}\n\n"
        
        current_date += timedelta(days=1)
    
    return all_page_text

if __name__ == "__main__":
    start_date_str = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    end_date_str = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    newspapers = {
        "Opinion": get_opinion_url,
        "El Deber": get_eldeber_url,
        "Los Tiempos": get_lostiempos_url
    }
    
    all_page_text = extract_content_for_date_range(start_date, end_date, newspapers)
    
    with open('page_content.txt', 'w', encoding='utf-8') as file:
        file.write(all_page_text)
    
    print("Contenido extraído y guardado en page_content.txt")
