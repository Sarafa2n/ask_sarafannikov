from django.shortcuts import render
from django.views.generic import View, TemplateView


class LogoutView(View):
    pass


class PageNotFound(TemplateView):
    template_name = "core/errors/404.html"
