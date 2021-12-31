from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Author,Book
from .forms import AvatarForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.data.get('name')
            title = form.data.get('title')
            birth_date = form.data.get('dob')
            avatar = form.files.get('avatar')
            Author.objects.create(
                name = name,
                title = title,
                birth_date = birth_date,
                avatar = avatar
            )
        else:
            print('form not valid')
    return HttpResponse('hello')
def author(request):
    return render(request,'uploads/author.html')
def book(request):
    pass