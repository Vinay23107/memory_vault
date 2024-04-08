from django.shortcuts import render, redirect, HttpResponse
from main.models import Vacation_name, Vacation_image
from django.contrib.auth.models import User
from django.contrib.auth import login, logout as ilogout, authenticate
# Create your views here.

def index(request):
    v_n= Vacation_name.objects.all()
    return render(request, 'index.html', {'v_n':v_n})

def vac_images(request):
    id=request.POST.get('id')
    v_n = Vacation_name.objects.get(pk=id)
    v_i = Vacation_image.objects.filter(v_name_id=id) 
    return render(request, 'images.html', {'v_i':v_i, 'v_n':v_n})

def mylogin(request):
    return render(request, 'login.html')

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        passx = request.POST.get("passx")
        user = authenticate(username=uname, password=passx)
        if user is not None:
            login(request, user)

            
            return redirect('index')
        else:
            
            return HttpResponse('Check Username or Password again')  
    return redirect('index') 

def logout(request):
    ilogout(request)

    return redirect('index')

def signup(request):
    return render(request, 'signup.html')

def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        
        passx = request.POST.get("passx")
        

       

        xuser = User.objects.create_user(username=uname, password=passx)
        xuser.first_name = fname
        xuser.last_name = lname
        xuser.save()
        # messages.success(request, "Your account has been created")
        print('success')
        return redirect("index")
    else:

        return HttpResponse("404 error") 

def add_album(request):
    if request.user.is_authenticated:

        return render(request, 'add_album.html') 

def handle_add_album(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            aname=request.POST.get('aname')
            pimage= request.FILES['pimage']
            v_name= Vacation_name(name=aname, image=pimage, user_id=request.user.pk)
            v_name.save()
            return redirect('my_album')  
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error")  



def my_album(request):
    if request.user.is_authenticated:
        v_n= Vacation_name.objects.filter(user_id=request.user.pk)
    
        return render(request, 'my_album.html', {'v_n':v_n})
    else:
        return redirect('mylogin')     


def edit_album(request):
    if request.user.is_authenticated:
        id=request.POST.get('id')
        a=Vacation_name.objects.get(pk=id)
        return render(request, 'edit_album.html', {'a':a}) 

def handle_edit_album(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id= request.POST.get('id')
            aname=request.POST.get('aname')
            pimage= request.FILES['pimage']

            v_n= Vacation_name.objects.get(pk=id)
            # v_n.pk=id
            v_n.name=aname
            v_n.image=pimage
            # v_name= Vacation_name(name=aname, image=pimage, user_id=request.user.pk)
            v_n.save()
            print(v_n.pk, id)
            return redirect('my_album')  
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error") 

def delete_album(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id= request.POST.get('id')
            v_n= Vacation_name.objects.get(pk=id)
            v_n.delete()
            return redirect('my_album')
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error")

def my_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            v_i= Vacation_image.objects.filter(v_name_id=id)
        
            return render(request, 'my_image.html', {'v_i':v_i}) 

def add_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            return render(request, 'add_image.html', {'id':id})         

def handle_add_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            vimage= request.FILES['vimage']
            v_i= Vacation_image(v_name_id=id, v_image=vimage)
            v_i.save()
            return redirect('my_album')  
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error")        

def edit_image(request):
    if request.user.is_authenticated:
        id=request.POST.get('id')
        a=Vacation_image.objects.get(pk=id)
        return render(request, 'edit_image.html', {'a':a}) 

def handle_edit_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id= request.POST.get('id')
            # aname=request.POST.get('aname')
            vimage= request.FILES['vimage']

            v_i= Vacation_image.objects.get(pk=id)
            # v_n.pk=id
            # v_i.name=aname
            v_i.v_image=vimage
            # v_name= Vacation_name(name=aname, image=pimage, user_id=request.user.pk)
            v_i.save()
            
            return redirect('my_album')  
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error") 

def delete_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id= request.POST.get('id')
            v_i= Vacation_image.objects.get(pk=id)
            v_i.delete()
            return redirect('my_album')
        else:

            return HttpResponse("404 error") 
    else:

        return HttpResponse("404 error")        

def view_image(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST.get('id')
            i= Vacation_image.objects.get(pk=id)
        
            return render(request, 'view_image.html', {'i':i})