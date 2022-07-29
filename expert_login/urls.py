from django.urls import path,include
from . import views

urlpatterns = [
    
    #path('', views.ex_myworks,name='ex_myworks'),
    #path('',views.ex_login),
    #path('',views.file),
    path('',views.test),
    #path('file_upload/', views.file_upload,name='file_upload'),
    path('expert_login/', views.ex_login_verification,name='expert_login'),
    path('accept/', views.accept ),
    path('module_creation/', views.module_creation,name="module_creation"),
    

    path('ex_home/', views.ex_home,name='ex_home'),
    path('ex_myworks/', views.ex_myworks,name='ex_myworks'),
    path('ex_review/', views.ex_review,name='ex_review'),
    path('ex_completed/', views.ex_completed,name='ex_completed'),

    path('project_close/', views.project_close,name="project_close"),

]