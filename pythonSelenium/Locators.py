from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "name").send_keys("RAHUL")
driver.find_element(By.ID, "exampleCheck1").click()

# select class provide the methods to handle the options in drop-down
dropdownGender = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdownGender.select_by_visible_text("Female")
dropdownGender.select_by_index(0)  # Male is selected by index


driver.find_element(By.NAME, "email").send_keys("test.email@test.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
