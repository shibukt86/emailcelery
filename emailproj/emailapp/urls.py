from django.urls import path,include
from . import views
urlpatterns = [
    path('test', views.index,name="index"),
    path('test2', views.test2,name="test2"),

]