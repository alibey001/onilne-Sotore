from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>> CRUD Product Model <<<<<<<<<< #
    path('get-product-items/', GetAllProductItems.as_view()),
    path('create-product-items/', CreateAllProductItems.as_view()),
    path('update-product-items/<int:pk>/', UpdateAllProductItems.as_view()),
    path('delete-product-items/<int:pk>/', DeleteAllProductItems.as_view()),
]