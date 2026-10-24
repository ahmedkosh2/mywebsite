from django.urls import path
from .views import personal_info

urlpatterns = [
    path('info/', personal_info, name='personal-info'),
]
