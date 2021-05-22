from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_css_selector("a[href='/windows']").click()
driver.find_element_by_link_text("Click Here").click()
childwindow= driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
#closing child window
driver.close()
parentwindow= driver.window_handles[0]
driver.switch_to.window(parentwindow)
assert "Opening a new window" in driver.find_element_by_tag_name("h3").text
