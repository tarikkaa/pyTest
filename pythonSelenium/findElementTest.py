
# driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class=ui-menu-item] a")
print(len(countries))

for countrie in countries:
    if countrie.text == "India":
        countrie.click()
        break
# .get_attribute("value") --- takes the value that was selected from the list and is present in the input field
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"