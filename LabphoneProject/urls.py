from django.contrib import admin
from django.urls import path
from repair import views

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerForm, name='registerForm'),
    path('UserDashboard/myRepairs/', views.myRepairs, name='myRepairs'),
    path('UserDashboard/', views.UserDashboard, name='UserDashboard'),
    path('', views.homepage, name='homepage'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
    # CRUD 
    path('UserDashboard/createNewRepair/', views.createNewRepair, name='createNewRepair'),
    path('UserDashboard/commonBugs/', views.commonBugs, name='commonBugs'),
    path('repair/<int:Repair_pk>', views.updateRepair, name='updateRepair'),
    path('repair/<int:Repair_pk>/done', views.doneRepair, name='doneRepair'),
    path('repair/<int:Repair_pk>/delete', views.deleteRepair, name='deleteRepair'),
]

