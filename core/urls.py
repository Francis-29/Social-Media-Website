from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),

    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
]
