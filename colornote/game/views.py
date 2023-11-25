from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_user(request):
    # checking request method
    if request.method=='POST':
        # getting button ids
        #signup_id=request.POST.get('signupSubmit',False)
        #signin_id=request.POST.get('signinSubmit',False)
        #print(signup_id)
        if "signupSubmit" in request.POST:
            # getting variables from html page
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]
            # creating new user
            new_user = User.objects.create_user(username=username,email=email,password=password)
            # saving new user
            new_user.save()
            # sending messages
            messages.success(request,"your account has been successfully created")
            
        elif "signinSubmit" in request.POST:
            #getting variables from html page
            username=request.POST['username']
            password=request.POST['password']
            # making an user variable
            user = authenticate(request,username="username",password="password")
            # checking if user not None
            if user!=None:
                login(request,user)
                return redirect("board")
        
    return render(request,"authenticate/login.html")

def board(request):
    return render(request,"game/board4.html")
