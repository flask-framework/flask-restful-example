import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from user.dbi import insert_admin_user

if __name__ == "__main__":
    username = input("请输入用户名5-20个字符：")
    password = input("请输入密码5-20个字符：")
    email = input("请输入邮箱：")
    phone = input("请输入电话号码：")
    insert_admin_user(username=username, password=password, email=email, phone=phone)
    print("创建完成！")
