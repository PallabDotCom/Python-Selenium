from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\debnpal\\Documents\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("iFrame").click()

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)