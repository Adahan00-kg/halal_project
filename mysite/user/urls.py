
from django.urls import path,include
from .views import *

urlpatterns = [
    path('user/',UserProfileListAPIView.as_view(),name = 'user_list'),

    path('user/<int:pk>/',UserProfileRetrieveUpdateAPIView.as_view(),name = 'user_detail'),

]