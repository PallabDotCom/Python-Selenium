import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.maximize_window()

productlist = []
productlist2 =[]

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(5)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    # going back to grand parent to select the expected product
    productlist.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(productlist)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()

SelectedVeggies= driver.find_elements_by_css_selector("p.product-name")

for SelectedVeggie in SelectedVeggies:
    productlist2.append(SelectedVeggie.text)

print(productlist2)

assert productlist != productlist2


driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

#Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
'''
You can click the element like below once it appears after wait
element = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
element.click()
'''


print(driver.find_element_by_css_selector("span.promoInfo").text)

