from django.contrib import admin

# Register your models here.
from .models import Student,Book,Post


admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Post)
