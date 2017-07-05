from django.db import models

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
    sex = models.IntegerField(choices=((1, "male"),
                                       (2, "female")), verbose_name="Płeć")


class Trening(models.Model):
    date = models.DateField()
    time = models.TimeField()
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    number = models.CharField(max_length=32, blank=None)
    distance = models.CharField(max_length=8)
    pace = models.IntegerField(choices=PACE)
    description = models.TextField(max_length=400)
    added_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person)


