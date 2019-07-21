import array as arr


# x = 2
# y = 5
#
# if x > y:
#     print("BIG")
# else:
#     print("Small")


# for x in range(5):
#     print(x)

# x = 2
# #
# # if x == 1:
# #     print('summer')
# # elif x == 2:
# #     print('winter')
# # elif x == 3:
# #     print('fall')
# # elif x == 4:
# #     print('spring')


# list1 = [43, 'Z', 3.6, True, 9]
# for x in list1:
#     print(x)
#     print(list1[0] + list1[2])

# myPhone = input("Enter phone number: ")
# print("phone number is ", myPhone)



def printHello():
    print('hello')


def calculate():
    print(5+3.2)


def printName(name, lastname):
    print(name, lastname)


def printNum(num1, num2):
    print(num1 + num2)


# a = arr.array("i", [3, 6, 9])
# for x in range(len(a)):
#     print(a[x])


# for x in range(5):
#     print('#' * x)

def getNum():
    usernum = input("Enter a number: ")
    # print(usernum)
    calcSum(usernum)


def calcSum(getnum):
    y = 0
    for x in range(len(getnum)):
        y += int(getnum[x])
    print("sum of", getnum, 'digits is', y)


if __name__ == '__main__':
    getNum()
    #     # printHello()
    #     # calculate()
    #     # printName('avi', 'zilbershtein')
    #     # printNum(6, 3)

