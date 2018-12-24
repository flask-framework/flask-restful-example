from user import views

urlpatterns = [
    # 登陆
    (views.Login, "/admin/api_v1/user/login/"),
    # 获取身份信息
    (views.GetSefProfile, "/admin/api_v1/user/profile/self/"),
    # 注销
    (views.Logout, "/admin/api_v1/user/logout/"),
    # 获取分组信息
    (views.GetGroupsByUser, "/admin/api_v1/user/groups/<int:user_id>/"),
    # 获取权限信息
    (views.GetPermissionsByGroup, "/admin/api_v1/user/permissions/"),
]
