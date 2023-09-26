
from django.http import HttpResponse
# Create your views here.
from .models import Product, User, LessonStatus


def index(request):
    return HttpResponse("Hello, this is index page for noobie school.")


def self_overall(request):
    user = request.user
    res = LessonStatus.objects.all().filter(User == user)
    outer = []
    for line in res:
        outer.append(
            [
                line.lesson,
                line.watched(),
                line.time_watching
            ]
        )
    return outer


def self_product(request, name):
    user = request.user
    res = LessonStatus.objects.all().filter(User == user).filter(Product.name == name)
    outer = []
    for line in res:
        outer.append(
            [
                line.lesson,
                line.watched(),
                line.time_watching,
                line.recent_seen
            ]
        )
    return outer


def overall(request):
    res1 = Product.objects.all()
    res2 = LessonStatus.objects.all()
    total_watch = 0
    users = len(list(User.objects.all()))
    users_with_access = 0
    res3 = Product.objects.all()
    for prod in res3:
        users_with_access += len(prod.access)
    for res in res2:
        total_watch += res.time_watching
    percentage = users_with_access/users
    res_viewed = []
    for prod in res1:
        res3 = [LessonStatus.objects.all().filter(LessonStatus.is_watched is True and LessonStatus.user in prod.access)]
        res_prod = (prod.name, len(res3))
        res_viewed.append(res_prod)
    return [res_viewed, total_watch, percentage]
