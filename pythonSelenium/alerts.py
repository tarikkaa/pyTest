from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

validateText = "Option3"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
   # click OK button
alert.accept()

   # click CANCEL button
#alert.dismiss()

