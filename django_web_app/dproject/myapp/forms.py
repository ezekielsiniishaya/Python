# myapp/forms.py
from django import forms
from .models import Book
from .models import CustomUser

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','publication_date', 'description', 'price']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'bio']