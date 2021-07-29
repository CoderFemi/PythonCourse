from selenium import webdriver
from pprint import pprint

chrome_driver_path = 'C:/Users/Femi/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get('https://www.python.org')
# event_times = driver.find_elements_by_css_selector('.event-widget time')
# event_names = driver.find_elements_by_css_selector('.event-widget li a')
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
# pprint(events)

driver.get('http://secure-retreat-92358.herokuapp.com/')
input_first = driver.find_element_by_name('fName')
input_last = driver.find_element_by_name('lName')
input_email = driver.find_element_by_name('email')

input_first.send_keys('Sam')
input_last.send_keys('Meena')
input_email.send_keys('meena@hotmail.com')
driver.find_element_by_tag_name('button').click()


# driver.close()  # Closes the current tab
# driver.quit()  # Closes the entire browser
