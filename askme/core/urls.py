from django.urls import path
from .views import LogoutView

app_name = 'core'

urlpatterns = [
    path('logout', LogoutView.as_view(), name="logout"),
]
