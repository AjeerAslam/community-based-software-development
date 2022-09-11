from django.urls import path,include
from clientlogin import views



urlpatterns = [
    path('',views.load,name='load'),
    #path('community_logi/', views.index ,name='index'),
    path('index1/', views.index1 ,name='index1'),
    path('logout/', views.logout1,name='logout' ),
    path('cosignup/',views.cosignup,name='cosignup'),
    path('csignup/', views.csignup,name='c_signup' ),
    path('accept/', views.accept ),
    path('cm_close/', views.cm_close ),
    
    path('cm_home/', views.index,name='cm_home'),
    path('cm_mywork/', views.cm_mywork,name='cm_mywork'),
    path('cm_review/', views.cm_review,name='cm_review'),
    path('cm_completed/', views.cm_completed,name='cm_completed'),
    path('cm_upload/', views.cm_upload,name='cm_upload'),

    path('cm_view/<int:pk>/', views.cm_view,name='cm_view'),
    path('ex_view/<int:pk>/', views.ex_view,name='ex_view'),
    path('cm_delete/<int:pk>/', views.cm_delete,name='cm_delete'),
   

]