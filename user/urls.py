from user import views

urlpatterns = [
    # 登陆
    (views.Login, "/admin/api_v1/user/login/"),
    # 获取身份信息
    (views.GetSefProfile, "/admin/api_v1/user/profile/self/"),
    # 注销
    (views.Logout, "/admin/api_v1/user/logout/"),
    # 获取用户分组
    (views.GetGroupsByUser, "/admin/api_v1/user/groups/<int:user_id>/"),
    # 获取用户列表，带有分页和其他搜索
    (views.UserList, "/admin/api_v1/user/list/"),
    # 用户查找、删除和更新操作
    (views.User, "/admin/api_v1/user/<int:user_id>/"),
    # 获取所有分组列表
    (views.GroupList, "/admin/api_v1/group/list/all/"),
]
