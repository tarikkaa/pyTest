# driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "name").send_keys("RAHUL")
driver.find_element(By.NAME, "email").send_keys("email@test.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")

driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
print(driver.find_element(By.CLASS_NAME, "alert-success").text)
# [class*='alert-success'] - CSS
# //*[contains(@class, 'alert-success')] - RegEx > xPath
