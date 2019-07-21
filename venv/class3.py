# try:
#     my_file = open("C:\\Users\\azilbers\\Documents\\avipy1.txt", 'r')
#     content = my_file.read()
#     print(content)
#
# # except IOError as x:
# #     print("fail to open file")
# #     print(x)
#
# # print(my_file)
#
# finally:
#     print("finished")
#
# print("123")
#
# # my_file.write("text added")
# # print(my_file.read())


# x = 3
# x = 5
# x = 7
# print(x)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\azilbers\\Documents\\mydrivers\\chromedriver.exe")
driver.get("https://translate.google.co.il/")
print(driver.current_url)
print(driver.title)
# driver.maximize_window()
translate = driver.find_element_by_id("source")
# txt.click()
translate.clear()
translate.send_keys("Avi Zilbershtein")
translate.send_keys(Keys.ENTER)
translate.send_keys("Thanks God")




print(translate.get_attribute("class"))


