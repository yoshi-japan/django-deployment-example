from django.urls import path
from basic_app import views

# template urls!
app_name = 'basic_app'

# in index.html, we use template tags that look like this {% url "basic_app:user_login" %}
# basic-app is the value of app_name, user_login is the valued assigned to name.
urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/',views.user_login,name='user_login'),

]