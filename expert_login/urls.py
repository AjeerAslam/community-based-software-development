from django.urls import path,include
from expert_login import views

urlpatterns = [
    
    #path('', views.ex_myworks,name='ex_myworks'),
    
    #path('',views.file),
    
    #path('file_upload/', views.file_upload,name='file_upload'),
    
    
    #login
    path('',views.ex_login,name='ex_login'),
    path('expert_login/', views.ex_login_verification,name='expert_login'),
    path('log_out/', views.log_out,name='log_out'),
    #path('expert_login/',views.download_file ,name='expert_login'),
    
    #projects
    path('ex_home/', views.ex_home,name='ex_home'),
        #path('accept/', views.ex_myworks,name='accept'),
        path('accept/', views.accept,name='accept'),
        path('description/<str:pk>/', views.description,name='description'),
        
    path('ex_myworks/', views.ex_myworks,name='ex_myworks'),
        path('project_close/', views.project_close,name='project_close'),
    path('ex_review/', views.ex_review,name='ex_review'),
    path('ex_completed/', views.ex_completed,name='ex_completed'),

    #modules
    path('ex_new_modules/',views.ex_new_modules,name='ex_new_modules'),
        path('module_creation/', views.module_creation,name="module_creation"),
        path('md_import/<str:pk>/', views.md_import,name="md_import"),
        path('md_description/<str:pk>/', views.md_description,name='md_description'),
    path('ex_manage_modules/',views.ex_manage_modules,name='ex_manage_modules'),
        path('approve_module/', views.approve_module,name='approve_module'),
        path('module_suggestion/', views.module_suggestion,name='module_suggestion'),
    path('ex_review_modules/',views.ex_review_modules,name='ex_review_modules'),
    path('ex_completed_modules/',views.ex_completed_modules,name='ex_completed_modules'),
    path('ex_import_modules/',views.ex_import_modules,name='ex_import_modules'),

    path('download_file/', views.download_file,name='download_file'),
    path('download_request/', views.download_request,name='download_request'),
    path('download_request_client/', views.download_request_client,name='download_request_client'),
    

     

]