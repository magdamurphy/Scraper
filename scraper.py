
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.airbnb.co.uk/rooms/19278160?s=51'
url2 = 'https://www.airbnb.co.uk/rooms/14531512?s=51'
url3 = 'https://www.airbnb.co.uk/rooms/19292873?s=51'

def run(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        prop_name = get_name(driver)
        prop_type = get_type(driver)
        no_of_beds = get_no_of_beds(driver)
        no_of_bathrooms = get_no_of_bathrooms(driver)
        click_aminities_button(driver)
        aminities = get_aminities(driver)
        property_info = {
            'Property Name': prop_name,
            'Property Type': prop_type,
            'Number of bedrooms': no_of_beds,
            'Number of bathrooms': no_of_bathrooms,
            'Amenities': aminities
        }
        print(json.dumps(property_info, sort_keys=False, indent=2))
    finally:
        driver.quit()

def get_name(driver):
    prop_name_xpath = '//*[@id="summary"]/div/div[1]/div[1]/div/div[1]/div[1]/div/span/span/h1'
    prop_name = driver.find_element_by_xpath(prop_name_xpath).text
    return prop_name

def get_type(driver):
    prop_type_xpath = '//*[@id="summary"]/div/div[1]/a/div/span/span/span'
    prop_type = driver.find_element_by_xpath(prop_type_xpath).text
    return prop_type

def get_no_of_beds(driver):
    no_of_beds_xpath = '//*[@id="summary"]/div/div[1]/div[2]/div/div[3]/div/div[2]/span'
    no_of_beds = driver.find_element_by_xpath(no_of_beds_xpath).text
    return no_of_beds

def get_no_of_bathrooms(driver):
    no_of_bathrooms_xpath = '//*[@id="summary"]/div/div[1]/div[2]/div/div[4]/div/div[2]/span'
    no_of_bathrooms = driver.find_element_by_xpath(no_of_bathrooms_xpath).text
    return no_of_bathrooms


def click_aminities_button(driver):
    aminities_button_xpath = '//*[@id="room"]/div/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div/section/div[3]/div/button'
    driver.find_element_by_xpath(aminities_button_xpath).click()

def get_aminities(driver):
    aminities_section_category_xpath = 'html/body/div[9]/div/div/div/div/div/div/div/section/div/section/div[%s]/div[1]'
    is_element = True
    element_index = 1
    aminities = {}
    while (is_element):
        try:
            category = driver.find_element_by_xpath(aminities_section_category_xpath%(element_index)).text
            names = get_aminity_category_names(driver, element_index)
            aminities[category] = names
            element_index += 1
        except NoSuchElementException:
            is_element= False
    return aminities

def get_aminity_category_names(driver, category_index):
    aminities_section_names_xpath = '/html/body/div[9]/div/div/div/div/div/div/div/section/div/section/div[%s]/div[2]/div[%s]/div[1]/div/div'
    is_element = True
    element_index = 1
    names = []
    while (is_element):
        try:
            name = driver.find_element_by_xpath(aminities_section_names_xpath%(category_index,element_index)).text
            names.append(name)
            element_index += 1
        except NoSuchElementException:
            is_element= False
    return names


run(url)
run(url2)
run(url3)
