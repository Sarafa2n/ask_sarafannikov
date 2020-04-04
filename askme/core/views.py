from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View, TemplateView


class ApiLogoutView(View):
    http_method_names = ['get']

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'auth',
                'message': 'User not authorized'
            })


class PageNotFound(TemplateView):
    template_name = "core/errors/404.html"


class ApiAuthView(View):

    def post(self, request):
        if request.user.is_authenticated:
            return JsonResponse({
                'status': 'auth',
                'message': 'User is authenticated'
            })
        else:
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({
                        'status': 'success'
                    })
            else:
                return JsonResponse({
                    'status': 'invalid',
                    'message': 'Sorry, wrong password',
                    'errors': form.errors
                })
