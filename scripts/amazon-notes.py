
import pdb
from selenium import webdriver

import config

print(config.username)

url = "https://read.amazon.com/"
url = "http://read.amazon.com/notebook"


driver = webdriver.Chrome()
driver.get(url)
driver.switch_to.default_content()



email = driver.find_element_by_id("ap_email")
email.send_keys(config.username)
password = driver.find_element_by_id("ap_password")
password.send_keys(config.password)

submit = driver.find_element_by_id("signInSubmit")
submit.click()




books = driver.find_elements_by_class_name("kp-notebook-searchable")

books[0].click()
pdb.set_trace()

highlights = driver.find_elements_by_id("highlight")
loc = driver.find_elements_by_id("annotationHighlightHeader")


"""

1. Get Highlight

highlights = driver.find_elements_by_id("highlight")



2. 


"""