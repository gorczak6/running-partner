from django.contrib import admin

# Register your models here.
from run.models import Person, Training, Comments

admin.site.register(Person)
admin.site.register(Training)
admin.site.register(Comments)
