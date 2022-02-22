from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/tar/Drivers/chromedriver")
'''
driver.get("https://rahulshettyacademy.com/AutomationPractice")
# Hover- ActionChains class should be imported and 'driver' should be put there
# .perform() method is used for action while hovering (even after .click())

action = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")
action.move_to_element(menu).perform()
childMenu = driver.find_element(By.LINK_TEXT, "Reload")
action.move_to_element(childMenu).click().perform()
'''

'''
# double-click action
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element(By.ID, "double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
'''
# action right click
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element(By.ID, "double-click")).perform()