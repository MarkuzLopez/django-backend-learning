from django.urls import path
from .views import (
    product_list_create,
    product_delete_put
)

urlpatterns = [
    path('products/', view=product_list_create),
    path('products/<int:pk>/', view=product_delete_put),
]