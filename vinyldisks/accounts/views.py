from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('productsdescription')

        else:
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)

    return redirect('login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Этот пользователь уже используется')
                return redirect('login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Этот E-mail уже используется')
                    return redirect('login')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'Вы успешно авторизовались')
                    return redirect('productsdescription')
        else:
            return redirect('register')
    else:
        return render (request, 'accounts/register.html')