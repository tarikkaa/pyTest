# Implicit wait

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
# Implicit wait is Global wait, all steps wait up to e.g. 5 sec or less (if elements loaded faster)
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
print(count)
assert count == 3
addButtons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in addButtons:
    button.click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
promoInfoText = (driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
print(promoInfoText)
assert (promoInfoText) == "Code applied ..!"