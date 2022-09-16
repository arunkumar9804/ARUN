from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from product.models import fashion_collection
a="php"
n="testing"
def index(request):
    pro=fashion_collection.objects.all()
    print(pro)
    return render(request,"index.html",{"pro":pro})

def samp(request):
        return render(request,"test.html",{'l':a,'m':n})

def login(request):
    if request.method=="POST":
        name=request.POST["uname"]
        pas=request.POST["pname"]
        user=auth.authenticate(username=name,password=pas)
        if user is not None:
             auth.login(request,user)
             return redirect("/")
        else:
            msg="invalid password and username"
            return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html")    
        

def register(request):
    if request.method=="POST":
        username=request.POST["uname"]
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        email=request.POST["mail"]
        password=request.POST["pas"]
        repassword=request.POST["repas"]
        uchk=User.objects.filter(username=username)
        echk=User.objects.filter(email=email)
        
        if uchk:
            na="username is alreadytaken"
            return render(request,"register.html",{"na":na})

        elif echk:
            na="email is already taken"
            return render(request,"register.html",{"na":na})
        elif password !=repassword: 
            na="invalid password"
            return render(request,"register.html",{"na":na})
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save();
            auth.login(request,user)
            return redirect('/')
 
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect(request,"test.html") 



 





# Create your views here.
