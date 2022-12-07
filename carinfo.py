from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
from random import randint
from time import sleep

def read_link_from_file(filename):
    car_list = []
    with open(filename, "r") as f:
        for line in f:
            car_list.append(line)
    return car_list

def get_car_data(driver):
    car_data = driver.find_element(By.CLASS_NAME, "full-side")
    price = car_data.find_element(By.CLASS_NAME, "prices").text
    # print(price)
    rest_elems = car_data.find_elements(By.TAG_NAME, "p")
    parameters = {}
    parameters.update({"Price": price})
    sleep(randint(1,3))
    for elem in rest_elems:
        if ":" in elem.text:
            elem_split = elem.text.split(":")
            elem_split[0] = elem_split[0].replace(" ", "_")
            parameters.update({elem_split[0]:elem_split[1]})
        elif "≈" in elem.text:
            elem_split = elem.text.split("≈")
            elem_split[0] = elem_split[0].replace(" ", "_")
            parameters.update({elem_split[0]:elem_split[1]})
    return parameters


if __name__ == "__main__":

    ################################################################
    # bidfax_url = "https://en.bidfax.info/audi/a3/15965673-audi-a3-sedan-premium-plus-2017-black-20-vin-wauj8gff9h1019070.html"
    # PATH = "/home/mateusz/ekspolracja_danych/chromedriver"
    # driver = webdriver.Chrome(PATH)
    # driver.get(bidfax_url)
    ###############################################################
    # car_data = driver.find_element(By.CLASS_NAME, "full-side")
    # price = car_data.find_element(By.CLASS_NAME, "prices").text
    # # print(price)
    # rest_elems = car_data.find_elements(By.TAG_NAME, "p")
    # parameters = {}
    # parameters.update({"Price": price})
    # for elem in rest_elems:
    #     if ":" in elem.text:
    #         elem_split = elem.text.split(":")
    #         parameters.update({elem_split[0]:elem_split[1]})
    #     elif "≈" in elem.text:
    #         elem_split = elem.text.split("≈")
    #         parameters.update({elem_split[0]:elem_split[1]})
    # print(parameters)
    ####################################################################
    car_data = []
    car_list  = read_link_from_file("audi.txt")
    car_list = car_list[:50]
    PATH = "/home/mateusz/ekspolracja_danych/chromedriver"
    driver = webdriver.Chrome(PATH)
    for link in car_list:
        driver.get(link)
        sleep(randint(1,3))
        param = get_car_data(driver)
        car_data.append(param)

    json_string = json.dumps(car_data)
    with open("audi_data2.json", "w") as file:
        file.write(json_string)
