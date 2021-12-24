from selenium import webdriver
# browser exposes an executable file
# though Selenium test we need to invoke the exe file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com")  # get method to hit url on browser
print(driver.title)
print(driver.current_url)

driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()