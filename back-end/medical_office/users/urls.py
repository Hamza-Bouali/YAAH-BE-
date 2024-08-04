from django.urls import path
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    AppointmentListCreateAPIView,
    AppointmentRetrieveUpdateDestroyAPIView,
    LoginView,
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('appointments/', AppointmentListCreateAPIView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyAPIView.as_view(), name='appointment-retrieve-update-destroy'),
     path('login/', LoginView.as_view(), name='login'),
]
