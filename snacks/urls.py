from django.urls import path
from .views import (
    SnackCreateView,
    SnackDeleteView,
    SnackDetailView,
    SnackListView,
    SnackUpdateView,
)

urlpatterns = [
    path('', SnackListView.as_view(), name='home'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack-detail'),
    path('create/', SnackCreateView.as_view(), name='create-snack'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='update-snack'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete-snack')
]
