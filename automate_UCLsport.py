from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import time
import sys
from datetime import datetime


try:
    with open("info.txt", "r") as fichier:
        lignes = fichier.readlines()
    username_str = lignes[0].strip().split("-")[1]
    password_str = lignes[1].strip().split("-")[1]
    programme = lignes[2].strip().split("-")[1]
    jour = lignes[3].strip().split("-")[1]
    heuredebut = lignes[4].strip().split("-")[1]
    heurefin = lignes[5].strip().split("-")[1]
    current_datetime = datetime.combine(datetime.now().date(), datetime.min.time())
    """Set up webdriver."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    geckodriver_path = os.path.join(os.getcwd(), "geckodriver.exe")
    driver_service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(options=options, service=driver_service)
    driver.get("https://sites.uclouvain.be/uclsport/register")
    #wait page has been charged
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    username = driver.find_element("id", "input-account")
    password = driver.find_element("id","input-password")
    username.send_keys(username_str)
    password.send_keys(password_str)

    buttons = driver.find_elements("tag name","button")
    connexion_path=""
    for button in buttons:
        if "CONNEXION" in button.text:
            driver.execute_script("arguments[0].click();",button) # connexion to website
    #wait until user is connected
    time.sleep(20)
    buttons = driver.find_elements("css selector","a[role = 'button']")
    for button in buttons:
        if ("date_range" in button.text):
            driver.execute_script("arguments[0].click();",button) # connexion to horaires 
    time.sleep(0.5)
    buttons = driver.find_elements("css selector","h6[class='mb-0 text-nowrap']")


    #get jour prochain
    for button in buttons:
        date_match = re.search(r'\d{2}/\d{2}/\d{4}', button.text)
        if date_match:
            date_string = date_match.group()
            date_object = datetime.strptime(date_string, "%d/%m/%Y") # convert to datetime
            if (current_datetime < date_object): # logiquement la date qu ils affiche et toujours la meme que current_datetime on va donc get le prochain lundi
                arrow = driver.find_element("css selector","a[class = 'btn btn-filter px-0']")
                while (jour not in button.text): #on avance jusque lundi prochain
                    driver.execute_script("arguments[0].click();",arrow)
                    time.sleep(0.1)

    body = driver.find_element("css selector","[class='body container']")
    containers = body.find_elements("css selector","[class='container my-2 bg-active']")
    #JESSE WHAT THE FUCK IS THAT

    for container in containers:
        a = container.find_element("css selector","[class='row align-items-center mr-sm-0 pr-sm-0 collapsed']")
        tab = a
        for elem in ['col-10','row','col-sm-9 my-1','text-left mx-0 px-0','mb-0']:
            a = a.find_element("css selector","[class='{0}']".format(elem))
        if (programme in a.text and heuredebut in a.text and heurefin in a.text and 'LLN' in a.text):
            driver.execute_script("arguments[0].click();",tab.find_element("css selector","[class='material-icons align-middle btn-filter']")) # click on the "expand tab"
            tab = container.find_element("css selector","[class='row align-items-center mr-sm-0 pr-sm-0 not-collapsed']")
            buttons = container.find_elements("xpath",".//*")
            for button in buttons:
                if ("btn btn-primary btn-block" in button.get_attribute("class") and button.text == "INSCRIPTION"):
                    driver.execute_script("arguments[0].click();",button)
except Exception as e:
    error_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "error.txt")
    with open(error_file_path, "a") as error_file:
        error_file.write(f"An error occurred: {str(e)}\n")
    sys.exit()
#wait for confirmation popup
time.sleep(2)
try:
    body = driver.find_element("css selector","[class='modal-footer']")
    buttons = body.find_elements("css selector","[type='button']")
    for button in buttons : 
        if 'CONFIRMER' in button.text:
            time.sleep(2)
            driver.execute_script("arguments[0].click();",button)
except Exception as e:
    print("you are already registered")
    error_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "error.txt")
    with open(error_file_path, "a") as error_file:
        error_file.write(f"An error occurred: {str(e)}\n")
finally:
    driver.quit()



