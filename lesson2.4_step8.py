from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
   
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")  
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()
    
    input = browser.find_element_by_tag_name("input").send_keys(
        str(math.log(abs(12*math.sin(int(browser.find_element_by_id("input_value").text)))))
        )
    browser.find_element_by_id("solve").click()
    

finally:
    time.sleep(15)
    browser.quit()