from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from .form import SignUpForm,LoginForm, PostForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,Contact
#from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
#from django.conf import settings
#from blogpro.settings import EMAIL_HOST_USER
from . import form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
#from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            con = Contact(name=name, email=email, message=message)
            con.save()
            messages.success(request, 'Send succesfully !!')
            form = ContactForm()
            return render(
            request,
            "contact.html",
            {'forms':form}
            )
    else:
        form = ContactForm(request.POST)
    return render(
        request,
        "contact.html",
        {'forms': form}
    )

#def contact(request):
#    sub = form.EmailForm()
#    if request.method == 'POST':
#        #name=request.POST["name"]
#        subject=request.POST["name"]
#        message=request.POST["message"]
#        email=request.POST["email"]
        
#        User = form.EmailForm(request.POST)
       
#        email_from = settings.EMAIL_HOST_USER
#        recipient_list = [email, ]
#        send_mail(subject, message, email_from, recipient_list )
#        messages.success(request, 'Send Successfully !!!')

     
#    return render(request, 'contact.html', {'forms':sub})




# Create your views here.
def home(request):
    posts = Post.objects.all()
    
    #print(posts.id)
    return render(
        request,
        'home.html',
        {'posts':posts}
    )

def about(request):
    return render(
        request,
        'about.html'

    )


def dashboard(request):   
    if request.user.is_authenticated:
        current_user = request.user
        posts = Post.objects.filter(user=current_user) 
    else:
        redirect('/login/') 
    return render(
        request,
        "dashboard.html",
        {'posts':posts}
    )

   

def user_signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully SignUp')
            form.save()
            form = SignUpForm(request.POST)
    else:                
        form = SignUpForm()
    return render(
        request,
        "signup.html",
        {'form' : form}
    )



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:        
            form=LoginForm()
    else:
        return HttpResponseRedirect('/dashboard/')
    return render(request,
    "login.html",
    {'form':form}
    )

def addpost(request):
    if request.user.is_authenticated:
        if request.method =="POST":

            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                decs = form.cleaned_data['decs']
            #here in last parameter I have set user 
                pst = Post(title=title, decs=decs, user=request.user)
                pst.save()
            #please add here redirect otherwise throw error after post save
                messages.success(request, "Blog Added successfully !!")

            form = PostForm()
            return render(
                request,
                "addpost.html",
                {'posts':pst}
            )

            
        else:
            form = PostForm()        
        return render(
            request,
            "addpost.html",
            {'form' : form}
        )
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    print(dir(request.session))
    logout(request)
    
    return HttpResponseRedirect('/')

def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)

        return render(
            request,
            "updatepost.html",
            {'form': form }
            )
    else:
        return  HttpResponseRedirect('/login/')


def deleting_cookie(request):
    name = request.session('name',default=Guest)
    del request.session['name']
    response = HttpResponse("We are now finally deleting the cookie which is set")
    response.delete_cookie('Learning')
    return render(request, "delc.html")
