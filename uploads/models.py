from django.db import models
from django.db.models import fields
from django.forms import ModelForm

# Create your models here.
class Author(models.Model):
    TITLE_CHOICE = [
        ('MR','Mr.'),
        ('MRS','Mrs.'),
        ('MS','Ms.'),
    ]
    name = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=3,choices=TITLE_CHOICE,null= True)
    birth_date = models.DateField(blank=True,null=True)
    avatar = models.ImageField(null=True,blank=True,upload_to='root/kk/')
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name','title','birth_date','avatar']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','authors']