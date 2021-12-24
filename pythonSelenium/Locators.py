# driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "name").send_keys("RAHUL")

