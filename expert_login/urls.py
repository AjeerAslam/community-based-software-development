from django.urls import path,include
from . import views

urlpatterns = [
    
    #path('', views.ex_myworks,name='ex_myworks'),
    #path('',views.load),
    #path('',views.file),
    #path('file_upload/', views.file_upload,name='file_upload'),
    path('expert_login/', views.index,name='expert_login'),
    path('accept/', views.accept ),
    path('module_creation/', views.module_creation,name="module_creation"),

    path('', views.ex_home,name='ex_home'),
    path('ex_myworks', views.ex_myworks,name='ex_myworks'),
    path('ex_review/', views.ex_review,name='ex_review'),
    path('ex_completed/', views.ex_completed,name='ex_completed'),

]