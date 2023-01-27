from django.urls import path
from .views import TransactionView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("transactions/", TransactionView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]