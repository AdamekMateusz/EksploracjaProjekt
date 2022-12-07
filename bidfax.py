from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

def get_car_urls(driver):
    cars_url = []
    car_on_page = driver.find_element(By.ID, 'dle-content')
    cars = car_on_page.find_elements(By.CLASS_NAME, 'col-xs-12')
    sleep(randint(1,5))
    for car in cars:
        if len(car.find_elements(By.CLASS_NAME, "caption")) > 0:
            # link = car.find_element(By.CLASS_NAME, "caption").find_element(By.CLASS_NAME, "clearfix").find_element(By.PARTIAL_LINK_TEXT, 'bidfax')
            link = car.find_element(By.CLASS_NAME, "caption").find_element(By.TAG_NAME, "a")
            print(link.get_attribute('href'))
            sleep(randint(1,5))
            cars_url.append(str(link.get_attribute('href')))
    return cars_url

bidfax_url = "https://en.bidfax.info/audi/a3/f/from-year=2017/to-year=2017/page/"
PATH = "/home/mateusz/ekspolracja_danych/chromedriver"
driver = webdriver.Chrome(PATH)
# bidfax_url += "1/"

all_cars = []
# url = bidfax_url + "{}/".format(i)
driver.get(bidfax_url)
for i in range(2, 3):
    all_cars.extend(get_car_urls(driver))
    driver.get(bidfax_url + "{}/".format(i)) 
# all_elem = elem.find_elements('p')
# print(all_elem.get_attribute("innerHTML"))
# print(elem.get_attribute("innerHTML"))/\
driver.quit()

with open("bidfaxlink.txt", "w") as f:
    for link in all_cars:
        f.write(link + "\n")