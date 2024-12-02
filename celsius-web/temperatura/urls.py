from django.urls import path
from .views import index, temperatura, temperatura_delete, temperatura_edit

urlpatterns = [
    path('', index, name='index'),
    path('temperatura/', temperatura, name='temperatura'),
    path('temperatura/delete/<int:id>/', temperatura_delete, name='temperatura_delete'),
    path('temperatura/edit/<int:id>/', temperatura_edit, name='temperatura_edit'),
]