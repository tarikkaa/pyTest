# driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("RAHUL")  # In css_selector use "#" when it is "ID" attribute
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("Passw0rd")  # In css_selector use "." when it is "CLASS" attribute
driver.find_element(By.CSS_SELECTOR, ".password").clear()
# Use "LINK_TEXT" when the element has in HTML tag "a" (means link)
#driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
# Xpath with any text    //tagname[text()='sometext']
driver.find_element(By.XPATH, "//a[text()='Forgot Your Password?']").click()
driver.find_element(By.NAME, 'cancel').click()
