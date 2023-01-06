# coding=utf-8


class Test:
    def num1(self):
        global a
        a = 2



    def num2(self):
        print(a)

Test().num1()
Test().num2()
