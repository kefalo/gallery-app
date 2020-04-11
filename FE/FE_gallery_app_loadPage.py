from selenium import webdriver

driver = webdriver.Firefox(drivers/geckodriver.exe)

driver.set_page_load_timeout(10)
driver.get("https://gallery-app.vivifyideas.com/")
driver.find_element_by_class_name("title-style").send_keys("Page Loaded Successfully")
driver.find_element_by_class_name("form-control").click()

print("Page Loaded successfully")