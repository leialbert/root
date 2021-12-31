from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Author,Book
from .forms import AvatarForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST,request.FILES)
        name = form.cleaned_data.get('name')
        print('hello - ' + name)
        if form.is_valid():
            print(form)
        else:
            print('form not valid')
    return HttpResponse('hello')
def author(request):
    return render(request,'uploads/author.html')
def book(request):
    pass