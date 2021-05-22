#Java Script document object model(DOM) can access any elements on webpage just like selenium
#Selenium have a method to execute javascript in it.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
#selenium will not print anything using text method
print(driver.find_element_by_name("name").text)
#selenium is going to print, no matter 'value' is keyed by developer or not
print(driver.find_element_by_name("name").get_attribute("value"))
#JS will return the value , selenium is giving the control by execute_script method
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
#you can pass as many as argument with action
driver.execute_script("arguments[0].click();",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")



