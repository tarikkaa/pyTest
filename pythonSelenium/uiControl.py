import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# checkboxes have type="checkbox"
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.NAME, "radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

inputField = driver.find_element(By.ID, "displayed-text")
assert inputField.is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert not inputField.is_displayed()