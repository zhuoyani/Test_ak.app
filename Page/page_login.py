from selenium.webdriver.common.by import By
from Base.base import Base

# loc为元组，值有没有括号pycharm都可以识别为元组，注意：无括号时两个值以上为元组
loc_username = (By.ID, "com.vcooline.aike:id/etxt_username")
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"

class PageLogin(Base):
    """
        Page页面思路：
            1. 一个页面一个对象 (新建一个Class)
            2. 对象页面内需要操作的步骤，每一个步骤单独封装一个方法
    """
    # 输入用户名
    def page_input_username(self,text):
        # 调用的base类 封装的输入方法  因为继承Base，所以直接通过self.xxxx
        self.base_input(loc_username,text)
    # 输入密码
    def page_input_password(self,text):
        self.base_input(loc_pwd, text)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(loc_login_btn)