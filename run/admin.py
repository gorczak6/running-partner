from django.contrib import admin

# Register your models here.
from run.models import Person, Training, Comment

admin.site.register(Person)
admin.site.register(Training)
admin.site.register(Comment)
