from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

PACE = ((1, "wolniej niż 7:00/km"),
        (2, "6:45 - 7:00/km"),
        (3, "6:30 - 6:45/km"),
        (4, "6:15 - 6:30/km"),
        (5, "6:00 - 6:15/km"),
        (6, "5:45 - 6:00/km"),
        (7, "5:30 - 5:45/km"),
        (8, "5:15 - 5:30/km"),
        (9, "5:00 - 5:15/km"),
        (10, "4:45 - 5:00/km"),
        (11, "4:30 - 4:45/km"),
        (12, "4:15 - 4:30/km"),
        (13, "4:00 - 4:15/km"),
        (14, "3:45 - 4:00/km"),
        )


class Person(models.Model):
    name = models.CharField(max_length=128, verbose_name="Imię/Pseudonim")
    sex = models.IntegerField(choices=((1, "mężczyzna"),
                                       (2, "kobieta")), verbose_name="Płeć")

    def __str__(self):
        return self.name


class Training(models.Model):
    date = models.DateField(verbose_name="data")
    time = models.TimeField(verbose_name="godzina")
    city = models.CharField(max_length=64, verbose_name="Miejscowość")
    street = models.CharField(max_length=64, verbose_name="Ulica/miejsce")
    number = models.CharField(max_length=32, blank=True, verbose_name="Numer")
    distance = models.CharField(max_length=8, verbose_name="Dystans")
    pace = models.IntegerField(choices=PACE, verbose_name="Tempo")
    description = models.TextField(max_length=400, verbose_name="Krótki opis")
    added_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.date, self.time, self.city, self.distance, self.author)


class Comment(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='autor', on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=400, verbose_name='komentarz')
    created_date = models.DateTimeField(default=timezone.now)
    training = models.ForeignKey('Training', related_name='comments', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.author, self.txt, self.created_date)


class UserLogin(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


