from django.urls import path

from .views import homePageView, register, login_user, logout_user, forgotten, recover, change_password

urlpatterns = [
    path('', homePageView, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('forgottenpassword/', forgotten, name='forgotten'),
    path('forgottenpassword/recover/', recover, name='recover'),
    path('changepassword/', change_password, name='change'),
]