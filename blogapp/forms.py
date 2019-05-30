from django import forms
from .models import Student, Book, Post


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade', 'address', 'image', 'email']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'isbn',
                  'created_date', 'book_published', 'issued_by', 'price']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image',
                  'date_created', 'author']
