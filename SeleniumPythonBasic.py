from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")
driver.implicitly_wait(5)
'''
driver.get("https://book.spicejet.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

driver.get("https://www.amazon.ca/")
driver.back()
driver.refresh()
'''

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Static drop down with select class

dropdown = Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_index(2)
option = dropdown.first_selected_option.text
assert "Option2" in option

#Auto suggestive drop down

driver.find_element_by_id("autocomplete").send_keys("ag")
places = driver.find_elements_by_xpath("//ul[@class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front']/li")
for place in places:
    if place.text == "Paraguay":
        place.click()
        break
assert driver.find_element_by_id("autocomplete").get_attribute('value') == "Paraguay", "Test passed"

#Select Checkbox dynamically
checkboxes= driver.find_elements_by_xpath("//input[@type='checkbox']")
checkboxes[2].click()
assert checkboxes[2].is_selected()

#Select Radio button dynamically
Radiobuttons= driver.find_elements_by_xpath("//input[@type='radio']")
for Radiobutton in Radiobuttons:
    if Radiobutton.get_attribute('value')=='radio1':
        Radiobutton.click()
        assert Radiobutton.is_selected()

#Handle Java pop ups
Text= "pallab"
driver.find_element_by_css_selector("input[id='name']").send_keys(Text)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert Text in alert.text
alert.accept()
'''
For cancel or rejection use this method
alert.dismiss()
'''

#Check Displayed edit box

print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed())
#driver.close()








