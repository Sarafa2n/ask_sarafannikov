from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View, DetailView, ListView, TemplateView
from .models import Question, Tag, Answer, Vote
from .utils import pagination


class IndexView(ListView):
    template_name = "pages/index.html"
    model = Question
    ordering = '-created_dt'
    paginate_by = 3
    context_object_name = 'questions_list'


class TagView(ListView):
    template_name = "pages/index.html"
    model = Tag
    context_object_name = 'tag_list'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag = self.kwargs.get('slug')
        tag_obj = get_object_or_404(Tag, title=tag)
        context['page_obj'] = pagination(
            Question.objects.all().filter(tag=tag_obj).order_by('-created_dt'),
            self.request
        )
        return context


class SettingsView(TemplateView):
    template_name = "pages/settings.html"


class HotView(ListView):
    template_name = "pages/index.html"
    queryset = Question.objects.get_hot()
    paginate_by = 3
    context_object_name = 'questions_list'


class AskView(TemplateView):
    template_name = "pages/ask.html"


class LoginView(View):
    http_method_names = ['get']

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('pages:index')
        else:
            return render(request, 'pages/login.html')


class SingUpView(View):
    http_method_names = ['get']

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('pages:index')
        else:
            return render(request, 'pages/singup.html')


class QuestionDetailView(DetailView):
    template_name = "pages/question-detail.html"
    model = Question
    context_object_name = 'question_detail'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answers'] = self.object.answer_set.all().filter(is_published=True)
        return context
