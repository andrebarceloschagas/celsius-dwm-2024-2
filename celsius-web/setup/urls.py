from django.contrib import admin
from django.urls import path, include
from setup.views import Index, Login, Logout, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    
]
