from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
driver.get("https://the-internet.herokuapp.com/iframe")

# iframe, frameset, frame (frame tags in HTML)
# frame id or frame name or index value is used
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("I can automate!")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)