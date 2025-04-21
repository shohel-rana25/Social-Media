from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm , ProfileForm
from .models import ProfileModel
from Posts .models import PostModel
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def myprofile(request):
#     profile = ProfileModel.objects.get(user=request.user)
#     myposts = PostModel.objects.filter(profile=profile).order_by('-created_at')
#     return render(request, 'myprofile.html', {'profile': profile, 'myposts': myposts})

@login_required
def myprofile(request):
    profile = ProfileModel.objects.get(user=request.user)
    myposts = PostModel.objects.filter(profile=profile).order_by('-created_at')

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'myprofile.html', {'profile': profile, 'myposts': myposts, 'form': form})

    


# @login_required
# def profile_photo(request):
#     profile = ProfileModel.objects.get(user=request.user)  # get current user's profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('myprofile')
#     else:
#         form = ProfileForm(instance=profile)
#     return render(request, 'myprofile.html', {'form': form})


def edit_profile(request):
    # Get the current user's profile
    profile = ProfileModel.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('profile')  # Redirect to profile page (or wherever you want)
    else:
        form = ProfileForm(instance=profile)  # Prepopulate the form with current profile data

    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})


def change_profile(request):
    profile = ProfileModel.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save the new profile picture
            return redirect('myprofile')  # Redirect to the profile page after upload
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'myprofile.html', {'form': form, 'profile': profile})