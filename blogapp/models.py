from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150)
    grade = models.PositiveIntegerField()
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="students")
    email = models.EmailField()

    def __str__(self):
        return self.name
        # return '%s %s' %(self.name, self.id)


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    isbn = models.BigIntegerField()
    created_date = models.DateTimeField(default=timezone.now(), blank=True)
    book_published = models.DateField(blank=True, null=True)
    # issued_by 	= models.ManyToManyField(Student)
    issued_by = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(
        max_digits=19, decimal_places=4, default=400.30)

    def __str__(self):
        return '%s %s %s' % (self.id, self.title, self.author)

    # def publish(self):
    # 	self.book_published = timezone.now()
    # 	self.save()


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="news_photo")
    date_created = models.DateTimeField(default=timezone.now(), blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
