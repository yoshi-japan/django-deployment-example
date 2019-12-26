from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


# this decorator is awesome to make sure any view requires a person to be logged in to see it.
# all you do is just decorate it with this log in required.
# the decorator should be called directly one line above.
@login_required
def user_logout(request):
    logout(request)
    # reverse back to the indexpage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # user.set_password(user.set_password) this I said first. jose has different code.
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                # i made a typo of 'profile.pic'
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,
                  'basic_app/registration.html',
                  {
                      'user_form':user_form,
                      'profile_form':profile_form,
                      'registered':registered
                  })


# don't use names of function that are already used from import, it's going to overwrite them!
# in this case, login is already used so we'll make it a little more unique so that call it user_login.
def user_login(request):

    if request.method == 'POST':
        # in input in html, we use name='username' attribute, so we use get('username') method.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django sometimes complains if you pass in just username, password so actually tell it the variable
        # username=username, password=password.
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # thanks ot a lot of built-in function in Django, we just say login function we imported.
                login(request,user)

                # once they're logged in, you send them somewhere. what we're doing here is
                #  we'll reverse them to index page when they successfully login and account is active.
                return HttpResponseRedirect(reverse('index'))
            # if their account is not active,
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
        # on 'this if user call' we say else, and we might want to print out something like for us to notice.
        else:
            print("Someone tried to login and failed!")
            # this is what they tried to log in with. this username and password is not already in our database.
            print('Username:{} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied!')

    else:
        return render(request,'basic_app/login.html',{})
