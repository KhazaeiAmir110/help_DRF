from django.contrib import admin

from .models import Person, Questions, Answer

admin.site.register(Person)
admin.site.register(Questions)
admin.site.register(Answer)
