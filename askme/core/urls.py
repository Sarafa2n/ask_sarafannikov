from django.urls import path
from .views import ApiLogoutView, ApiAuthView

app_name = 'core'

urlpatterns = [
    path('logout', ApiLogoutView.as_view(), name="api_logout"),
    path('login', ApiAuthView.as_view(), name="api_login"),
]
