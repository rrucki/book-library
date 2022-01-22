from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new/', views.add_new, name='add_new'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('api/', views.api, name='api'),
    path('save_changes/<int:pk>', views.save_changes, name='save_changes'),
    path('delete/<int:pk>', views.delete, name='delete')
]
