from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
driver_path = r"C:\Users\carov\Desktop\CLASES CODING\V2\Clase 127 v2\OK OK\chromedriver"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,210):
        print(f'Extrayendo página {i+1} ...' )
        
        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Bucle para encontrar los elementos usando XPATH
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
           
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

    print(planets_data[1])

# Llamada del método
scrape()


