class Example:

    # def fun1(self):
    #     print("hello world")


    def passfunc():
        for letter in 'Python':
            if letter == 'h':
                pass
                print("pass block")
            print('current letter ', letter)


if __name__ == '__main__':
    # Example().fun1()
    Example.passfunc()

