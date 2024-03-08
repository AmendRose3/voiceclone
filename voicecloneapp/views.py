from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test
import pyttsx3


def index(request):
    return render(request,'index.html')

def register(request):
    form=defaultform()
    form2=regform()
    mydict={'form':form,'form2':form2}
    if request.method=='POST':
        form=defaultform(request.POST)
        form2=regform(request.POST)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,'SUCCESSFULLY REGISTERED')
            regmodel=form2.save(commit=True)
            regmodel.user=user
            regmodel.save()
            group=Group.objects.get_or_create(name="Userpage")
            group[0].user_set.add(user)
            return redirect('login')
    return render(request,'register.html',context=mydict)

def is_regmodel(user):
    return user.groups.filter(name="Userpage").exists()

def login(request):
    return render(request,'login.html')

def afterlogin_view(request):
    if is_regmodel(request.user):
        u=str(request.user)
        request.session['user']=u
        return redirect('userpage')

@login_required(login_url="login")
@user_passes_test(is_regmodel)
def userpage(request):
    u=request.session['user']
    return render(request,'userpage.html',{'u':u})


@login_required(login_url="login")
@user_passes_test(is_regmodel)
def profile(request):
    pro=regmodel.objects.get(user_id=request.user.id)
    if request.method=="POST":
        pro=regmodel.objects.get(user_id=request.user)
        pro1=defaultform(request.POST,instance=pro.user)
        pro2=regform(request.POST,instance=pro)
        if pro1.is_valid() and pro2.is_valid():
            user=pro1.save()
            user.set_password(user.password)
            user.save()
            pro2.save()
            return redirect('login')
    else:
         pro1=defaultform(instance=pro.user)
         pro2=regform(instance=pro)
         context={
            'pro1':pro1,
            'pro2':pro2
         }
    return render(request,'profile.html',context)     

@login_required
def logout_request(request):
    logout(request)
    return redirect('/')

def tts(request):
    if request.method=="POST":
        data=request.POST['speak']
        print('data is',data)
        message=data
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            print(voice, voice.id)
            engine.setProperty('voice', voice.id)
            engine.say(message)
        # engine.say(message)
        engine.runAndWait()
        return render(request,'tts.html')
    return render(request,'tts.html')