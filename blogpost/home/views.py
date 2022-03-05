from django.shortcuts import render, redirect
from .models import Blogs
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

previous = ''

def main(request):
    return redirect('home')

def home(request):
    blogs = Blogs.objects.all()
    sorted_blogs = sorted(blogs, key= lambda x: x.id, reverse=True)
    
    user_id = request.user.id
    user_blogs = Blogs.objects.filter(user_id=user_id)
    recent_activity = sorted(user_blogs, key= lambda x: x.id, reverse=True)
    return render(request,'index.html', {'blogs': sorted_blogs,'recents':recent_activity})

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                # print(user)
                auth.login(request, user)
                # previous = request.META['HTTP_REFERER']
                print(previous)
                
                return redirect('/')
            else:
                messages.info(request, 'invalid credentials')
                return redirect('login')
        else:
            # print('username does not exist')
            messages.info(request, 'username does not exist')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

 
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # print(username,email,password1,password2)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email is already linked')
                return redirect('register')
            else:
                # print('user created')
                user = User.objects.create_user(username=username,email=email,password=password1)
                # user.save()
                # time.sleep(1)
                return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def create(request):
    user_id = request.user.id
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES['img']
        description = request.POST['description']
        # form = Blogs(request.POST, request.FILES)
        
        # img_object = form.instance
        # print(img_object)
        b = Blogs(title=title, img=img, description=description, user_id=user_id)
        b.save()
        return redirect('/')
    else:

        if request.user.is_authenticated:
            
            return render(request, 'create.html')
        else:
            return redirect('login')

def myfeed(request):
    previous = request.META['HTTP_REFERER']
    print(f'myfeed - {previous}')
    
    if request.user.is_authenticated:

        user_id = request.user.id
        user_blogs = Blogs.objects.filter(user_id=user_id)
        sorted_userblogs = sorted(user_blogs, key= lambda x: x.id, reverse=True)
        return render(request, 'myfeed.html', {'blogs': sorted_userblogs})
    else:
        return redirect('login')
