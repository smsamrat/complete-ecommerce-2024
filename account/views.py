from django.shortcuts import render, redirect
from account.forms import UserCreateForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from account.models import Profile, Size
from account.forms import ProfileForm
# Create your views here.

def user_signup(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {
        "form":form
    }
    return render(request,"account/signup.html",context)

def user_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user_name,password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                pass
                # Non-specific error message (security)
                # form.add_error(None, 'Invalid username or password.')

    context = {

        "form":form
    }
    return render(request,"account/login.html",context)

def user_logout(request):
    logout(request)
    return redirect("login")


def  user_profile(request):
    # if request.method == "POST":
    #     size = request.POST.get('size')
    #     print(size,"daffdfadsad*****")
    profile = Profile.objects.get(user=request.user)
    sizes = Size.objects.all()
    context = {
        "profile":profile,
        "sizes":sizes,
    }
    return render(request,"account/user_profile_show.html",context)



def user_profile_update(request):
    form = ProfileForm()
    profile_instance = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=profile_instance)
        if form.is_valid():
            form.save()
    context ={
        "form":form
    }
    return render(request,"account/user_profile.html",context)




