import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
'''
#mouse Hover
menu=driver.find_element_by_id("sub-menu")
action.move_to_element(menu).perform()
childmenu=driver.find_element_by_link_text("Google")
action.move_to_element(childmenu).click().perform()

driver.back()
'''
#context & double click
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()