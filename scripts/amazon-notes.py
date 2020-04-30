
import pdb
from selenium import webdriver

import config


url = "http://read.amazon.com/notebook"

def login(url):

    driver = webdriver.Chrome()
    driver.get(url)
    driver.switch_to.default_content()
    email = driver.find_element_by_id("ap_email")
    email.send_keys(config.username)
    password = driver.find_element_by_id("ap_password")
    password.send_keys(config.password)

    submit = driver.find_element_by_id("signInSubmit")
    submit.click()
    return driver





def gatherHighlights(driver):
    books = driver.find_elements_by_class_name("kp-notebook-searchable")

    results = {}
    content = []

    for i in range(4):
        pdb.set_trace()
        if i % 2 == 0:
            content = []
            books[i].click()
            highlights = driver.find_elements_by_id("highlight")
            loc = driver.find_elements_by_id("annotationHighlightHeader")
            for hi in range(4):
                b = books[i].text
                a = books[i+1].text
                l = loc[hi].text.split("|")[1].split(":")[1].strip()
                t = loc[hi].text.split("|")[0]
                n = highlights[hi].text
                content.append([b,a,l,t,n])

        else:
            results[books[i-1].text] = content
            content = []
            continue



    return results



'''







            #add it
            content.insert(books[i].text,1)
            results.append(content)
            content = []
            continue
        else:
            content.append[books[i].text]
            books[2].click()
            highlights_kpi = driver.find_elements_by_id("kp-notebook-highlights-count").text
            content.append(highlights_kpi)
            notes_kpi = driver.find_elements_by_id("kp-notebook-notes-count").text
            content.append(notes_kpi)
            content.append([])
            highlights = driver.find_elements_by_id("highlight")







    books[2].click()

    highlights_kpi = driver.find_elements_by_id("kp-notebook-highlights-count")
    notes_kpi = driver.find_elements_by_id("kp-notebook-notes-count")



    #highlights = driver.find_elements_by_id("highlight")
    #loc = driver.find_elements_by_id("annotationHighlightHeader")
    
    '''

driver = login(url)

print(gatherHighlights(driver))


"""

1. Get Highlight

highlights = driver.find_elements_by_id("highlight")



2. 


"""