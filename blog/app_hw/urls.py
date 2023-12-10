from django.urls import path
from app_hw.views import *

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('detail/<int:post_id>/', detail_page_view, name='detail_page'),
    path('create/', create_page_view, name='create_page'),
]