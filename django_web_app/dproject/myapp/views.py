from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .models import CustomUser
from .forms import UserForm
from .forms import BookForm
from django.http import JsonResponse
from django.middleware.csrf import get_token


def json_view(request):
    data = {'message': 'Hello, JSON!'}
    return JsonResponse(data)  # Returns JSON instead of HTML
def http_response(request):
     return HttpResponse("Welcome to my django app")
def home(request):
     return render(request, 'myapp/index.html')
# display the books from the database

####from .models import Book

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'myapp/book_list.html', {'books': books})

def user_profile(request):
    users = CustomUser.objects.all()
    return render(request, 'myapp/user_profile.html', {'users': users})

def add_book(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        price = request.POST.get('price')
        description = request.POST.get('description')

        # Create a new book record
        try:
            author = CustomUser.objects.get(id=author)
            book = Book.objects.create(
                title=title,
                author=author,
                publication_date=publication_date,
                price = price,
                description=description
            )
            print(f'New book added: {book}')
            return redirect('book_list')  # Redirect to book list page
        except CustomUser.DoesNotExist:
            return HttpResponse("Selected author does not exist", status=400)
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=400)
    else:
        users = CustomUser.objects.all()
        return render(request, 'myapp/add_book.html', {'users': users})

def creat_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
            form = UserForm()
    return render(request, 'myapp/create_user.html', {'form': form})
    

# view for csrf requsts

def csrf(request):
    if request.method == 'GET':
        # Get CSRF token for the session
        csrf_token = get_token(request)
        return JsonResponse({"csrfToken": csrf_token})
    return JsonResponse({"error": "Only GET method allowed"}, status=400)