from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://flights-app.pages.dev/")  
from_input = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
to_input = driver.find_element(By.ID, "headlessui-combobox-input-:Rqhlla:")

def test_list_number_sameCity(str1,str2):
    
    from_input = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
    to_input = driver.find_element(By.ID, "headlessui-combobox-input-:Rqhlla:")
    from_input.send_keys(str1)
    time.sleep(0.1)
    from_input.send_keys(Keys.ENTER)
    to_input.send_keys(str2)
    time.sleep(0.1)
    to_input.send_keys(Keys.ENTER)

    try:
        message_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".mt-24.max-w-5xl.w-full.justify-center.items-center.text-sm.lg\\:flex")))
        
        message_text = message_element.text
        if message_text == "Bu iki şehir arasında uçuş bulunmuyor. Başka iki şehir seçmeyi deneyebilirsiniz.":
            print("You cant choose same cities BUG!")
        else:
            print("Success!")
    except TimeoutException: 
        print("")
        
    from_input.clear()
    to_input.clear()
    from_input.send_keys(str1)
    time.sleep(0.1)
    from_input.send_keys(Keys.ENTER)
    to_input.send_keys(str2)
    time.sleep(0.1)
    to_input.send_keys(Keys.ENTER)

    try:
        items_text = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//p[contains(@class, "mb-10")]')))
        flight_count = int(items_text.text.split()[1])

        elements = WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.overflow-hidden.rounded-xl.border.border-gray-200"))
        )


        if flight_count == len(elements):  
            print("Found X items are correct!")
        else:
            print("Found X items are not correct!")
    except TimeoutException:
        print("")

    from_input.clear()
    to_input.clear()


unique_countries =  ["FCO", "LHR", "ORD", "IST", "CDG", "HND", "SYD", "JFK", "DXB", "PEK", "LAX", "SIN", "MAD", "FRA", "HKG", "MAD"]
      
for i in unique_countries:
    for j in unique_countries:
        test_list_number_sameCity(i,j)
        
driver.quit()