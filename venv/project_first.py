import selenium

import time
driver = selenium.webdriver.Chrome(executable_path="C:\\Users\\azilbers\\Documents\\mydrivers\\chromedriver.exe")
driver.implicitly_wait(10)

#read URL from external file
my_file = open("C:\\Users\\azilbers\\Documents\\Jenkins\\url_site.txt", 'r')
url_site = my_file.read()
driver.get(url_site)
driver.maximize_window()

# register_site = driver.find_element_by_link_text("הרשמה")
register_site = driver.find_element_by_class_name("seperator-link")
register_site.click()
# time.sleep(3)
# driver.quit()

# click להרשמה
driver.find_element_by_class_name("text-btn").click()

print("change done 7/22")

#register page
driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("Avi")
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("user@test.local")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("Password1!")
driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("Password1!")
checkbox_elements = driver.find_elements_by_xpath("//input[@type=checkbox]")
for x in range(checkbox_elements):
    checkbox_elements[x].click()

driver.find_element_by_xpath("//button[@type='submit']")
driver.find_element_by_class_name("chosen-single").find_element_by_link_text('עד 99 ש"ח')

# driver.find_element_by_xpath("//input[text=("אני מסכים לתנאי ")]")
# driver.find_element_by_link_text("אני מסכים לתנאי").click()
# driver.find_element_by_link_text("הרשמה ל-BUYME").click()














