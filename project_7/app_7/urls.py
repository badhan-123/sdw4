
from django.urls import path
from . import views
# from app_7.views import home

urlpatterns = [
    path('',views.home,name='home' ),

]
