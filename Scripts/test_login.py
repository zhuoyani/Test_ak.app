import os,sys

import allure

sys.path.append(os.getcwd())
# 位置
from Base.read_yaml import get_yaml
import pytest
from Base.get_driver import get_driver
from Page.page_login import PageLogin

def get_data():
    arrs=[]
    for i in get_yaml().values():
        arrs.append((i.get("username"),i.get("password"),i.get("expect_toast")))
    return arrs



class TestLogin():
    # 初始化方法
    def setup_class(self):
        # 实例化 PageLogin
        self.login=PageLogin(get_driver())
    # 结束方法
    def teardown_class(self):
        # 关闭驱动对象
        self.login.driver.quit()
    # 测试方法
    @pytest.mark.parametrize("username,password,expect_toast",get_data())
    def test_login(self,username,password,expect_toast):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(password)
        print("预期结果为：",expect_toast)
        # 点击登录
        allure.attach("描述：","点击登录按钮")
        self.login.page_click_login_btn()
if __name__ == '__main__':
    pytest.main("-s test_login.py")

    """
        需求：
            1. 登录数据("18600001111,123456",",234567")
            2. 使用参数化
            3. 数据存储文件使用yaml
    """