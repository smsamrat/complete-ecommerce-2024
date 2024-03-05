from django.urls import path
from account.views import user_signup,user_login, user_logout, user_profile_update, \
    user_profile
urlpatterns = [
    path("signup/",user_signup,name="signup"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path("user-profile-update/",user_profile_update,name="user_profile_update"),
    path("user-profile-show/",user_profile,name="user_profile_show"),

]