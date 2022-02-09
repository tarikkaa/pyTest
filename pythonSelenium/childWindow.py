from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
# Tabs are handled like alist ("parent","child")
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

