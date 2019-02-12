from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    # 修改app名字为中文
    verbose_name = '用户管理'
