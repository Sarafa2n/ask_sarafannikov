from django.urls import reverse
from django.db import models
from core.models import Profile
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


class Vote(models.Model):

    CHOICES_KIND_LIKE = 1
    CHOICES_KIND_DISLIKE = -1

    CHOICES_KIND = (
        (CHOICES_KIND_LIKE, 'like'),
        (CHOICES_KIND_DISLIKE, 'dislike')
    )

    kind = models.IntegerField(choices=CHOICES_KIND)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey('Answer', null=True, blank=True, on_delete=models.CASCADE)

    @property
    def value(self):
        value_map = {
            self.CHOICES_KIND_LIKE: 1,
            self.CHOICES_KIND_DISLIKE: -1,
        }
        return value_map.get(self.kind, 0)


class QuestionManager(models.Manager):

    def get_hot(self):
        return super(QuestionManager, self).get_queryset().\
            annotate(vote_sum=Coalesce(Sum('vote__kind'), Value(0))).order_by('-vote_sum')


class Question(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    tag = models.ManyToManyField('Tag', default=None)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:question', args=[self.id])

    def has_like_from(self, user):
        return self.vote_set.filter(user=user).exists()

    @property
    def rating(self):
        return sum(map(lambda x: x.value, self.vote_set.all()))

    @property
    def answers_count(self):
        return self.answer_set.all().count()


class Tag(models.Model):

    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:tag', args=[self.title])


class Answer(models.Model):

    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, default=None)
    created_dt = models.DateField(auto_now_add=True, blank=True, null=True)
    correct = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return "Ответ на {} {}".format(self.question, self.id)

    @property
    def rating(self):
        return sum(map(lambda x: x.value, self.vote_set.all()))
