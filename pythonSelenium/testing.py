from selenium import webdriver
# browser exposes an executable file
# though Selenium test we need to invoke the exe file which will then invoke actual browser
# ("C:\ChromeDriver\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")

weight = float(input('Enter your weight, please:'))
height = float(input('Enter your height, please:'))
result = weight / height**2
if result < 18.5:
    print('Underweight')
elif 18.5 <= result < 25:
    print('Normal')
elif 25 <= result < 30:
    print('Overweight')
elif result >= 30:
    print('Obesity')

