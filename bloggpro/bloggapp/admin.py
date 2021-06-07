from django.contrib import admin
#from .form import Contact
from .models import Post,Contact
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','decs']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']