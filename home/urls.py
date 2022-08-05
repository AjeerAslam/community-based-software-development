from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.index, name='home'),
    #path('', views.test, name='home'),
    path('signup/', views.communitysignup, name='sign'),
    path('login/', views.login, name='log'),
    path('progress/', views.client_progress, name='progress'),
    path('requirement/', views.cl_requirement, name='req'),
    path('review/', views.cl_review, name='review'),
    path('complete/', views.cl_completed, name='complete'),
    path('accept/', views.accept ),
    path('log_out/', views.log_out, name='log_out'),


    path('expert/',include(('expert_login.urls','expert_login'),namespace='expert')),
    path('community/',include(('clientlogin.urls','clientlogin'),namespace='community')),
    #path('client',include('clientlogin.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)