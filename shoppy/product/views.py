from django.shortcuts import render,redirect

from .models import comment_box, fashion_collection

def about(request):
    id=request.GET['id']
    pro=fashion_collection.objects.get(id=id)
    print(pro)
    return render(request,"about.html",{'key1':pro})    

def comment(request):
    name=request.POST['user']
    message=request.POST['msg']
    product=request.POST['pro']
    cmt=comment_box.objects.create(name=name,msg=message,fkey_id=product)
    cmt.save();
    return redirect('/')
