# Explicit wait

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Explicit wait is NOT Global wait, it is used for one element only
# Needed to import WebDriverWait
exWait = WebDriverWait(driver, 7)  # now you can use this wait for every element separately

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
print(count)
assert count == 3
list_1 = []
list_2 = []
# Only xPath can reach elements from child to parent: //div[@class='product-action']/button/parent::div/parent::div/h4
addButtons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in addButtons:
    button.click()
    list_1.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
print(list_1)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list_2.append(veg.text)
    # it removes spaces "" from the list
    list_2 = [i for i in list_2 if i != ""]
print(list_2)

time.sleep(1)
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

print(sum)

totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == totalAmount

# needed to import expected_conditions

exWait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

exWait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
promoInfoText = driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text
print(promoInfoText)
assert (promoInfoText) == "Code applied ..!"

