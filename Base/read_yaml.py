import yaml,sys,os
def get_yaml():
    with open(os.getcwd()+os.sep+"Data"+os.sep+"login_data.yaml","r",encoding="utf-8")as f:
        return yaml.load(f)

def get_yaml1():
    with open("../Data/login_data.yaml","r",encoding="utf-8")as f:
        return yaml.load(f)


if __name__ == '__main__':
    # print(get_yaml())

    """
        分析：
            1. @pytest.mark.parametrize("username,password,expect_toast",
            [("18600001111","123456","密码错误"),("","234567","请输入手机号！")])
            
    """
    arrs=[]
    for i in get_yaml1().values():
        arrs.append((i.get("username"),i.get("password"),i.get("expect_toast")))
    print(arrs)