from django.contrib import admin


# Register your models here.

# from .models import Student, Group
from .models.group_models import Group
from .models.student_models import Student
from .models.ispit_models import Ekzamen, Predmet, Prepad


admin.site.register(Student)

admin.site.register(Group)

admin.site.register(Ekzamen)
admin.site.register(Predmet)
admin.site.register(Prepad)