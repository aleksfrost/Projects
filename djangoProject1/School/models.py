from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'USERS'


class Product(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    access = models.ManyToManyField(User)

    class Meta:
        db_table = 'PRODUCTS'


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    video_length = models.IntegerField()

    product = models.ManyToManyField(Product)

    class Meta:
        db_table = 'LESSONS'


class LessonStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recent_seen = models.DateField()
    Watched = models.FloatField(default=0.8)
    is_watched = models.BooleanField(default=False)
    time_watching = models.IntegerField(default=0)

    def watched(self):
        if self.lesson.video_length * self.Watched <= self.time_watching:
            self.Watched = True
            return True
        else:
            return False

