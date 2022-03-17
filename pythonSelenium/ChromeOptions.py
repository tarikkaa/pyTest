from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")           # no Chrome window opened
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe", options=chrome_options)
# driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)