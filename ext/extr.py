import requests
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, send_file
import io

app = Flask(__name__)

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

def almacenar_frases(contenido, archivo_salida):
    lineas = contenido.split('\n')

    frases = []

    for linea in lineas:
        # Borrar las líneas que tienen menos de 3 palabras
        if len(linea.split()) <= 3:
            continue
        # Eliminar las palabras que tienen menos de 3 caracteres
        palabras = linea.split()
        palabras_filtradas = [palabra for palabra in palabras if len(palabra) > 4]
        linea_filtrada = ' '.join(palabras_filtradas)
        frases.append(linea_filtrada)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        for frase in frases:
            file.write(frase + '\n')

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']
        selected_newspapers = request.form.getlist('newspapers')
        
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return render_template('index.html', error="Invalid date format. Use YYYY-MM-DD.")
        
        newspapers_funcs = {
    "Opinión": get_opinion_url,
    "El Deber": get_eldeber_url,
    "Los Tiempos": get_lostiempos_url
}

        
        newspapers = {name: newspapers_funcs[name] for name in selected_newspapers}
        
        if not newspapers:
            return render_template('index.html', error="Please select at least one newspaper.")
        
        all_page_text = extract_content_for_date_range(start_date, end_date, newspapers)        
        if all_page_text:
            frases_output = 'frases.txt'            
            almacenar_frases(all_page_text, frases_output)
            # correr el programa comandos.py
            stdout, stderr = run_command('python comandos.py')
            print("Comandos stdout:", stdout)
            print("Comandos stderr:", stderr)
            return send_file(
                frases_output,
                as_attachment=True,
                download_name=frases_output,
                mimetype='text/plain'                
            )                       
        else:
            return render_template('index.html', error="No content was extracted for the given date range.")
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


