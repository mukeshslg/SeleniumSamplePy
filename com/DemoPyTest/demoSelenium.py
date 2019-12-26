import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WS
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/mukeshsah/PycharmProjects/SeleniumSamplePy/resource/chromedriver_mac")
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
'Explicit wait'
wait = WS(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'btnLogin')))
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
driver.quit()
