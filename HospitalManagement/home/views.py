from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from  .models import Departments,Doctors,time1
from .forms import BookingForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
   

    return render(request,"index.html",)


def about(request):
    #return HttpResponse("About Page")
    return render(request,"about.html")

def booking(request): 
     if request.method == "POST" :
         form = BookingForm(request.POST)
         if form.is_valid():
             form.save()
             
     

     form = BookingForm()
     dict_form = {
         'form' : form
     }


     return render(request, "booking.html",dict_form)



def doctors(request):
    dict_docs = {
        'doctors' :Doctors.objects.all()
    }


    return render(request,"doctor.html",dict_docs)


def contact(request):
    return render(request,"contact.html")



def department(request):
    dict_dept = {
        'dept':Departments.objects.all()
    }

    return render(request,"department.html",dict_dept)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('booking')
        # else:
        #     messages.info(request,"invalid User")
        #     return redirect('register')


    return render(request,'login.html')



def register(request):

    if (request.method=='POST'):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST.get('password')
        cpassword =request.POST.get('password1')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken already")
                return redirect('register')
              
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)        
                user.save()
                return redirect('login') 
            print("Registration compleated successfully")
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')

    return render(request,"registration.html")



def logout(request):
    auth.logout(request)

    return render("logout.html")