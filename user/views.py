from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout

from .forms import SignUpForm,LoginForm

# Create your views here.


def signup(request):

    if request.method=='POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, passwd=passwd)
            login(user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request,'pages/signup.html',context={
        'form':form
    })

def login_view(request):
    message = ''
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user  = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                message = f'Hoşgeldin {user.username}! Giriş yaptınız.'
                return redirect('/')
            else:
                message = 'Giriş Başarısız'
                return redirect('/signup')
            
    return render(request,'pages/login.html',context={
        'form':form,
        'message':message
    })

def logout_view(request):
    logout(request)
    return redirect('/user/login')

