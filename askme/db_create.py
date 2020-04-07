from pages.models import Question, Profile, Tag, Vote

profile = Profile.objects.filter(pk=1).first()

for i in range(10):
    tag = Tag.objects.create(title=i, slug=i)
    tag.save()


for i in range(10):
    question = Question.objects.create(title='question', content=i, profile=profile)
    if Tag.objects.filter(title=i).exists():
        question.tag.add(Tag.objects.filter(title=i).first())
    question.save()

question = Question.objects.filter(pk=1).first()
vote = Vote.objects.create(kind=1, user=profile, question=question)
vote.save()
