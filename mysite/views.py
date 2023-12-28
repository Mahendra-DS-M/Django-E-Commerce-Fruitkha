# In this file we can load our actual html content in the format of python functions
# This views module  in application folder

from django.shortcuts import render, redirect

# User authentication functions in django

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# To display authentication messages
from django.contrib import messages

# Loading Table Data

from . models import contactinfo, products

# Create your views here.

def index(request):
    return render(request, 'index_2.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def shop(request):

    details = products.objects.all()

    context = {'products':details}

    return render(request, 'shop.html', context)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):

    # Collecting Html form data input fields information using their names

    if request.method=='POST':
        fname = request.POST['name']
        fmail = request.POST['email']
        fcontact = request.POST['phone']
        fsubject = request.POST['subject']
        fmessage = request.POST['message']

        # Creating  row for the collected form data for contactinfo table in models.py
        # insider create (colname = formvalue)
        record = contactinfo.objects.create(name=fname, mail=fmail, contact=fcontact, subject=fsubject, message=fmessage)
        # Saving form data to database
        record.save()

    else:
        return render(request, 'contact.html')
    
    # Load data from Database Table
     
    data = contactinfo.objects.all()
    print(data)

    return render(request, 'contact.html', {"tabledata":data})

def singlenews(request):
    return render(request,'single-news.html')

def singleproduct(request):
    return render(request, 'single-product.html')

def user(request, uname):
    urlname = User.objects.get(username=uname)
    return render(request, 'user.html', {'uname':urlname})

def user_signup(request):

    # Connecting to signup page , collecting credentials
    if request.method == 'POST':
        uname = request.POST['name']
        uemail = request.POST['email']
        upassword = request.POST['pswd']
        ucnfpassword = request.POST['pswd2']


        # Writing logic for user signup
        if upassword==ucnfpassword:
            if User.objects.filter(username=uname).exists(): # checking for username existing
                messages.info(request, "User Already Exists")
                return redirect('signup')
            elif User.objects.filter(email=uemail).exists(): # checking for mail existing
                messages.info(request, "Email Already Exists")
                return redirect('signup')
            else:
                # Creating user if name and mail are unique
                user = User.objects.create_user(username=uname, email=uemail, password=upassword)
                user.save()
                messages.info(request, "User Created")
                return redirect('login')
        else:
            messages.info(request, "Passwords Not Match")
            return redirect('signup')
    else:
        return render(request, 'signuplogin.html')

def user_login(request):

    # Connecting to login page , collecting credentials

    if request.method=='POST':
        
        name = request.POST['loginname']
        password = request.POST['loginpswd']

        # User check & Login

        user = authenticate(request, username=name, password=password)
        if user is not None:
            messages.info(request, f"You are now logged in as {name}.")
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "User Not Found")
            return redirect('login')
    else:
        return render(request, 'signuplogin.html')
    
def user_logout(request):
    # Logout user
    logout(request)
    return redirect('/')

def order(request):
    return render(request, 'orders.html')

