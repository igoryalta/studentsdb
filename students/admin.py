from django.contrib import admin


# Register your models here.

# from .models import Student, Group
from .models.group_models import Group
from .models.student_models import Student

admin.site.register(Student)

admin.site.register(Group)