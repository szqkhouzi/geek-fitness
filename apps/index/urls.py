from django.urls import path
from .views import *

urlpatterns = [
    # path('',IndexView.as_view(), name='index'),
    # path('page/',IndexView.as_view(), name='index_page_views'),
    path('',index),
    # path('(\d{4}/\d{2}/\d{2})/(.*?)/',detail),
    path('test/', index_test_views),

]