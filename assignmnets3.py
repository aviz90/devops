# try:
#     a = 1 / 0
# except ZeroDivisionError:
#     print("error can't divide by 0 ")

# try:
#     x = 1
# finally:
#     print("finally")

# file = open("C:\\Users\\azilbers\\Documents\\temp\\words.txt", 'r+', encoding='UTF-8')
# # file.write("אבי")
# file_read = file.read()
# print(file_read)

from PIL import Image

img = Image.new('RGB', (60, 30), color = 'red')
img.save('pil_red.png')
