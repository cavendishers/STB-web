from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
                path('',views.Xy_change, name = 'change'),  #xy交换主界面
                path('changefinish',views.changement, name = 'finish'), #交换结果
                path('login',views.login,name = 'login'),  #登陆界面
                path('logout',views.logout,name='logout'), #登出
                path('re_name',views.Hsy,name='re'),
                path('index',views.index,name = 'index'),


]