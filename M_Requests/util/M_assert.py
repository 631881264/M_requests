import json
class Myassert:
    def is_contain(self, result, r):
        """判断一个字符是否在另外一个字符中"""
        flag = None

        if result in r:
            flag = True
        else:
            flag = False
        return flag

if __name__ == '__main__':
    print(Myassert().is_contain("5","45"))