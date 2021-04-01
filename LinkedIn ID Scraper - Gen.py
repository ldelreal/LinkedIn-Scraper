from selenium import webdriver
import time
import csv
import numpy as np

# Webdriver necessary for scripted action
driver = webdriver.Chrome(executable_path=r"PATH TO CHROMEDRIVER")

# Setting up output file
writer = csv.writer(open('OUTPUTFILE', 'w+'), delimiter=',', lineterminator='\n')

# Login Script
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key')
username.send_keys('USER EMAIL')
time.sleep(0.5)
password = driver.find_element_by_id('session_password')
password.send_keys('PASSWORD')
time.sleep(0.5)
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
time.sleep(1)

# Array for hrefs
hrefs = []

# Array for page 1-100
urls = np.arange(1, 101, 1)

# Big For Loop going through every page from the search URL starting at 1 ending at 101
for url in urls:
    url = driver.get('SEARCHURLWITH&PAGEATEND'+str(url))
    time.sleep(1.5)

    # Finding parent element
    parent = driver.find_elements_by_class_name("entity-result__image-1")
    time.sleep(1)
    # For Loop to find tag in element
    for block in parent:
        elements = block.find_elements_by_tag_name("a")
        time.sleep(1)
        # For Loop to find href attribute in subsequent class>tag
        for el in elements:
            hrefs.append(el.get_attribute("href"))

# Writes out all hrefs to output file, putting 1 href per row
for i in hrefs:
    writer.writerow([i])
