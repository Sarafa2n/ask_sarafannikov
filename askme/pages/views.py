from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "pages/index.html"


class TagView(TemplateView):
    template_name = "pages/index.html"


class SettingsView(TemplateView):
    template_name = "pages/settings.html"


class HotView(TemplateView):
    template_name = "pages/index.html"


class AskView(TemplateView):
    template_name = "pages/ask.html"


class LoginView(TemplateView):
    template_name = "pages/login.html"


class SingUpView(TemplateView):
    template_name = "pages/singup.html"


class QuestionDetailView(TemplateView):
    template_name = "pages/question-detail.html"

