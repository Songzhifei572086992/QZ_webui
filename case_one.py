import unittest
from datadriver import data_dr

class UnitCase(unittest.TestCase):

    def test_01(self):
        data_dr('Sheet3')
        print('这是测试用例1')

    def test_02(self):
        data_dr('Sheet2')

# if __name__ == '__main__':
#     unittest.main()
