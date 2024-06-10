from django.urls import path
from .views import (
    PushupsApiView,
    PushupsDetailApiView,
)

urlpatterns = [
    path('pushups/', PushupsApiView.as_view()),
    path('pushups/<int:user_id>/', PushupsDetailApiView.as_view()),
]