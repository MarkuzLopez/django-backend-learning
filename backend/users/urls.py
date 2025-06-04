from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    clients_list_create,
    client_detail_update_delete,
)

urlpatterns = [
    # path('users', UserViewSet),    
    path('clients/', view=clients_list_create),
    path('clients/<int:pk>/', view=client_detail_update_delete),
    path('users/',  UserViewSet.as_view(), name='list-user-create')
]