from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 = request.POST['psw-repeat']

        if psw == psw2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=psw)
                user.save()
                return redirect('signin')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
         return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']

        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials!')
            return redirect('signin')
    else:

        return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
