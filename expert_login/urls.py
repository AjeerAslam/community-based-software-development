from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.load),
    path('',views.file),
    #path('file_upload/', views.file_upload,name='file_upload'),
    path('expert_login/', views.index,name='expert_login'),
    path('accept/', views.accept ),
    path('module_creation/', views.module_creation,name="module_creation"),

]