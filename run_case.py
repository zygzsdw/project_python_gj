
import unittest
import sys
from HTMLTestRunner import HTMLTestRunner

user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]
result = {'code':0,'message':''}

def login(username,password):

    # 如果用户名为空或密码为空，给出用户名或密码不能为空
    if username is None:
        result.update({'code': 1, 'message': '用户名不能为空'})
        return result
    if password is None:
        result.update({'code': 1, 'message': '密码不能为空'})
        return result

    # 如果用户名和密码匹配，返回登录成功且还有列表
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({'message':'登录成功','user_list':user_list})
            return result

    #如果不匹配，返回用户名或密码不正确 ，code返回1。
    result.update({'code': 1, 'message': '登录失败，请检查您的用户名或密码是否填写正确。'})
    return result




class TestLogin(unittest.TestCase):


    # # 初始化方法
    # def setUp(self) -> None:
    #     print("开始运行用例",sys._getframe().f_code.co_name)

    # case1 : 输入正确的用户名和正确的密码进行登录
    def test_login_success(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    def test_login_success1(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('dev','123456').get('code')
        self.assertEqual(except_value,actual_value)


    # case2 : 输入错误的用户名或密码进行登录
    def test_user_password_wrong(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin','1234567').get('code')
        self.assertEqual(except_value,actual_value)


    # case3 : 输入空的用户名或密码
    def test_user_password_null(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login_success'))
    suite.addTest(TestLogin('test_user_password_wrong'))
    suite.addTest(TestLogin('test_user_password_null'))
    test_report = './test_report.html'

    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告试用版')
        runner.run(suite)