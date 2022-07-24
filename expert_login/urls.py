from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.load),
    path('expert_login/', views.index ),
    path('accept/', views.accept ),
    path('module_creation/', views.module_creation ),

]