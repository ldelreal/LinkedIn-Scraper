from selenium import webdriver
import time
import csv

driver = webdriver.Chrome(executable_path=r"PATH TO CHROMEDRIVER")


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

# Creating Table of LinkedIn URLS
linkedin_urls = []

# Setting up writer for output
writer = csv.writer(open('NAMEOFOUTPUTFILE.csv', 'w+'), delimiter=',', lineterminator='\n')
# Setting up titles for rows
writer.writerow(['Name', 'Prev Company'])

# Reads list of IDs into Python, appends array with info
with open('test_info.csv') as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        linkedin_urls.append(row[0])

# Big For Loop, will go through each URL in created array
for url in linkedin_urls:
    url = driver.get(str(url))
    time.sleep(1.5)

    # this gets the person's name
    name = driver.find_element_by_class_name('pv-top-card--list').text
    time.sleep(1)

    # This is big experience section
    previous_company_parent = driver.find_elements_by_class_name('pv-profile-section__card-item-v2')
    time.sleep(1)
    # Creating an array for past experience
    prev_company = []
    # For loop to look within big experience section to find <a> tag
    for block in previous_company_parent:
        elements = block.find_elements_by_tag_name("a")
        time.sleep(1)
        # For loop to pull href from subsequent <a> tag
        for el in elements:
            prev_company.append(el.get_attribute("href"))
            time.sleep(0.5)
    # Writes name and second company from experience section to output csv
    writer.writerow([name, prev_company[1]])
