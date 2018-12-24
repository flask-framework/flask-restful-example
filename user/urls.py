from user import views

urlpatterns = [
    (views.Login, "/admin/api_v1/user/login/"),
    (views.GetSefProfile, "/admin/api_v1/user/profile/self/"),
    (views.Logout, "/admin/api_v1/user/logout/"),
]
