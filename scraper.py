import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
import selenium
from selenium.webdriver.common.by import By
import time
import random
RANDOM_TIME=[3,5,7,9,6,8]

class Scrapper():
    def __init__(self,city_name, max_rent):
        self.data_dict={}
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver=selenium.webdriver.Chrome(self.chrome_options)
        self.driver.get('https://www.storia.ro/ro/rezultate/inchiriere/apartament/toata-romania')
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/div/div/div/input').click()
        self.search_bar = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/input')
        self.search_bar.send_keys(city_name)
        time.sleep(random.choice(RANDOM_TIME))
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div/form/div[2]/div[1]/fieldset/div/label[2]').click()
        self.input_rent=self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div/form/div[2]/div[1]/fieldset/div/label[2]')
        self.input_rent.send_keys(max_rent)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="search-form-submit"]').click()
        self.page_source = self.driver.page_source
        self.scrape()
        self.driver.quit()
    def scrape(self):
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
        self.list_of_title=[]
        self.list_of_price=[]
        self.list_of_locations=[]
        self.list_of_links=[]

        # self.list_of_title_tag=self.soup.find_all('p', class_="css-u3orbr e1g5xnx10")
        self.list_of_price_tag=self.soup.find_all('span', class_="css-2bt9f1 evk7nst0")
        self.list_of_locations_tag=self.soup.find_all('p', class_='css-42r2ms eejmx80')
        self.list_of_links_tag=self.soup.find_all('div', class_='css-13gthep eeungyz2')
        for i in range(len(self.list_of_price_tag)):
           # self.list_of_title.append(self.list_of_title_tag[i].text)
           self.list_of_locations.append(self.list_of_locations_tag[i].text)
           self.list_of_price.append(self.list_of_price_tag[i].text.split('\xa0')[0])
           self.list_of_links.append(self.list_of_links_tag[i].find('a').attrs['href'])
        self.data_dict={
            'price':self.list_of_price,
            'location':self.list_of_locations,
            'links':self.list_of_links
        }






