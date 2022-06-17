from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.posted, name='posted')
]

handler404 = 'posts.views.page_not_found'