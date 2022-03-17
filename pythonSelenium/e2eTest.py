import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice")
wait = WebDriverWait(driver, 7)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        # Add item into cart
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("ind")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText
# make screenshot
driver.get_screenshot_as_file("false_screen.png")






