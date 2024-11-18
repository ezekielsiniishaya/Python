# myapp/forms.py
from django import forms
from .models import CustomUser, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','publication_date', 'description', 'price']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'bio']
Book = Book.objects.all()