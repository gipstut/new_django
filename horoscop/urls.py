from django.urls import path
from horoscop import views


urlpatterns = [
    path('html/', views.get_html),
    path('', views.index),
    path('<int:a>/', views.get_push_zodiac_number),
    path('<a>/', views.get_push_zodiac, name='horoscope-name'),

]