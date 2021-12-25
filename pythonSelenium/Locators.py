from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "name").send_keys("RAHUL")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.NAME, "email").send_keys("test.email@test.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
