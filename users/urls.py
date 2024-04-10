from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_page_view, name = 'signup'),
    path('signup/verify', views.verify_signup_view, name = 'verify_signup'),
    path('login/', views.login_page_view, name='login'),
    path('login/verify/', views.verify_login_view, name='verify_login'),
]
