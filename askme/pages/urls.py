from django.urls import path
from .views import IndexView, HotView, TagView, QuestionDetailView, SingUpView, AskView, LoginView, SettingsView

app_name = 'pages'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hot/', HotView.as_view(), name='hot'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('login/', LoginView.as_view(), name='login'),
    path('singup/', SingUpView.as_view(), name='singup'),
    path('ask/', AskView.as_view(), name='ask'),
    path('question/<int:pk>', QuestionDetailView.as_view(), name='question'),
    path('tag/<int:pk>', TagView.as_view(), name='tag')
]
