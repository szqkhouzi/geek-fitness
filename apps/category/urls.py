from django.urls import path
from .views import cate

urlpatterns = [
    path('cate/',cate)
]