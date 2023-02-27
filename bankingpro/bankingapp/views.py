from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import detail


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newform')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User()
                user.username = username
                user.password = password

                user.save()
                return redirect('login')

        else:
            print("password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def newform(request):
    return render(request, "newform.html")


def detailform(request):
    if request.method == 'GET':
        return render(request, "form2.html")
    else:
        try:
            if request.method == 'POST':
                name = request.POST.get('name')
                dob = request.POST.get('dob')
                gender = request.POST.get('gender')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                address = request.POST.get('address')
                district = request.POST.get('dropdown')
                sub = request.POST.get('new_dropdown')
                if not sub:
                    sub = request.POST.get('my_dropdown')
                if not sub:
                    sub = request.POST.get('my_dropdown_')
                if not sub:
                    sub = request.POST.get('ds_dropdown')
                if not sub:
                    sub = request.POST.get('pk_dropdown')
                account = request.POST.get('account')
                materials = request.POST.get('debitcard')
                if not materials:
                    materials = request.POST.get('creditcard')
                if not materials:
                    materials = request.POST.get('cheque')
                detail_obj = detail.objects.create(name=name, dob=dob, gender=gender, phone=phone, email=email,
                                                   address=address, district=district, subd=sub, account=account,
                                                   materials=materials)
                detail_obj.save()

                return redirect("/")

        except Exception as e:
            print(str(e))
            # details=detailform(name=name,dob=dob,phone=phone,email=email,address=address,district=district)

    return render(request, "form2.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
