from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UploadImageModelForm, UserRegistrationForm,UpdateUserProfileForm
from .models import Profile,User,Image,Follow

# Create your views here.
@login_required(login_url='login')  
def welcome(request):
    current_user = request.user
    posts = Image.objects.all()
    print(posts)
    try:
        user = User.objects.get(username = current_user.username)
        users = User.objects.exclude(username=current_user.username).exclude(is_superuser=True)
    except:
        user = None
        users = None
    context = {
        'posts':posts,
        'user':user,
        'users':users,     
        }

    return render(request,'index.html',context)
@login_required(login_url='login')
def dm(request):
    return render(request,'dm.html')
@login_required(login_url='login')
def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadImageModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = current_user
            form.save()
            return redirect('/')
    else:
        form = UploadImageModelForm()
    return render(request,'image_upload.html',{'form':form})
@login_required(login_url='login')
def explore(request):
    return render(request,'explore.html')
@login_required(login_url='login')
def notification(request):
    return render(request,'notification.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)
@login_required(login_url='login')
def profile(request):
    current_user = request.user
    user = User.objects.get(id = current_user.id)
    profile=Profile.filter_profile_by_id(user.id)
    posts = Image.objects.filter(user = user.id)
    return render(request,'profile.html',{'profile':profile,'posts':posts})

@login_required(login_url='login')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    if request.method == "POST":
            form = UpdateUserProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile') 
            else:
                return render(request,'update_profile.html',{'form':form})
    else:        
        form = UpdateUserProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form':form})
@login_required(login_url='login')
def follow(request,id):
    if request.method == 'GET':
        user_follow=User.objects.get(pk=id)
        follow_user=Follow(follower=request.user, followed=user_follow)
        follow_user.save()
        return redirect('user_profile' ,username=user_follow.username)
@login_required(login_url='login')    
def unfollow(request,id):
    if request.method=='GET':
        user_unfollow=User.objects.get(pk=id)
        unfollow_user=Follow.objects.filter(follower=request.user,followed=user_unfollow)
        unfollow_user.delete()
        return redirect('user_profile' ,username=user_unfollow.username)
@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', user_id=request.user.id)
    user_posts = user_prof.profile.posts.all()
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False

    context ={
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
         }
    
    return render(request, 'user_profile.html', context)