from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls import reverse
def homepage(request):
    return render(request,'navbar.html')

def about(request):
    # return HttpResponse("hello world"),
     return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return HttpResponse("contact me page for contacting")

def loginpage(request):
    username=''
    # return render(request,'login.html')
    if request.method=='POST':
        username=request.POST.get('username').strip()
        password=request.POST.get('password').strip()

        if  not username or  not password:
            messages.error(request,'Enter the information')
            return render(request,'login.html',{'username':username})
        
        user=authenticate (request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Entererd Successfully')
            return redirect('chai:all_chai')
        else:
            messages.error(request,'Login Failed!')
            return render(request,'login.html',{'username':username})
    return render(request,'login.html',{'username':username})





# def loginpage(request):
#     if request.session.get('failed_attempt',0)>=3:     # Check if the user has reached the max number of login attempts
#         messages.error['try again']
#         return render(request,'login.html')

#     else :
#         request.method=='POST'
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username ,password=password)          # Try to authenticate the user


#         if user is not None:   # The user exists and credentials are correct
#             login(request, user)
#             request.session('failed attempts')==0
#             return redirect('/chai')
#         else: # Increment failed attempts counter
#             failed_attempt = request.session('failed_attempts')+=1
#             return render(request,'login.html',{'error':'Try Again'})
        
#       #  if failed_attempt=request.session(failed_attempt)>==3: 
#         if failed_attempt>=3: 
#             messages.error(request,'Try after some time')
#         return render(request,'login.html')
    
    # def loginpage(request):
    #     if request.method=='POST':
    #         username=request.POST.get('username')
    #         password=request.POST.get('password')
    #         user=authenticate(request,username=username,password=password)
            

    #         if user is None: #this mean if the data is not correct
    #             # failed_attempts=request.session.get('failed_attempts',0)
    #             # failed_attempts+=1 #increment failed attempts
    #             # request.session['failed_attempts']=failed_attempts  #update failed attempts
    #             # # print("username:",username)
    #             # # print("password:",password)
    #             # # print("authenticating")

    #             # if failed_attempts>=3:
    #             messages.error(request,'Try again after some time')
                
    #         else:
    #             messages.error(request,"invalid credentials")
    #             return render(request,'login.html')
            
    #     else:
    #             print("login successful")
    #             request.session['failed_attempts']=0
    #             login(request,user)
    #             return redirect(reverse('chai:all_chai'))
        
    #     return render(request,'login.html')