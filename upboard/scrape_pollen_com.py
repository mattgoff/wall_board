from selenium import webdriver
import requests
import time

pollen_dict = {}
url = "http://www.goff.us/api/pollencount/1/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token)}

def send_info():
    response = requests.put(url, headers=head, data=pollen_dict)
    data = response.json()
    print(data)

def get_pollen_info():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')

    driver = webdriver.Chrome('/home/ubilinux/auto_py/chromedriver', chrome_options=options)
    driver.get('https://www.pollen.com/forecast/current/pollen/85383')
    allergyData = driver.find_element_by_css_selector("div#forecast-chart")
    time.sleep(5)
    data = allergyData.text.split("\n")
    time.sleep(5)
    pollen_dict["pollen_yesterday"] = str(data[2])
    pollen_dict["pollen_today"] = str(data[5]) + " " + ' '.join(data[8:11])
    pollen_dict["pollen_tomorrow"] = data[-2]

get_pollen_info()
send_info()



