# JS DOM can access any elements on web page just like how selenium does
# Selenium has a method to execute JavaScript code in it

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)    # this text can't be retrieved because it was input by selenium
print(driver.find_element(By.NAME, "name").get_attribute("value")) # this can retrieve the text even if there is no attribute 'value' in HTML

print(driver.execute_script('return document.getElementsByName("name")[0].value')) # or can retrieve the text by using JS exec

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)
# scroll page from the beginning to the end
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")