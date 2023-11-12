from django.urls import path

from studentapp import views

urlpatterns = [
    path('log',views.login_fun,name='log'),
    path("",views.home),
    path('reg',views.sign_fun,name='reg'),
    path('home',views.home_fun,name='home'),
    path('add',views.add_fun,name='add'),
    path('display',views.display,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('logout',views.logout,name='logout')

]