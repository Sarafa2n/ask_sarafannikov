from django.contrib import admin
from .models import Question, Answer, Vote, Tag


class QuestionsList(admin.ModelAdmin):
    fields = ('title', 'content', 'profile', 'tag')


admin.site.register(Question, QuestionsList)
admin.site.register(Answer)
admin.site.register(Vote)
admin.site.register(Tag)

