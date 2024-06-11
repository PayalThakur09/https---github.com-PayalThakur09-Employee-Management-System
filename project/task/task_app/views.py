from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Employee, Teamleader, Manager, User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_manager:
                login(request, user)
                return redirect('manager')
            elif user is not None and user.is_teamleader:
                login(request, user)
                return redirect('teamleader')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('/')

def admin(request):
    return render(request,'admin.html')

def manager(request):
    return render(request,'manager.html')

def teamleader(request):
    return render(request,'teamleader.html')

def employee(request):
    return render(request,'employee.html')

def meeting(request):
    return render(request,'meeting.html')

def project(request):
    return render(request,'project.html')

def team(request):
    return render(request,'team.html')

def teams_man(request):
    return render(request,'teams_man.html')

def teams_tl(request):
    return render(request,'teams_tl.html')

def allemployees(request):
    context={}
    e=Employee.objects.filter(is_active=True)
    print(e)
    context['employees']=e
    return render(request,'allemployees.html',context)

def allteamleaders(request):
    context={}
    t=Teamleader.objects.filter(is_active=True)
    print(t)
    context['teamleaders']=t
    return render(request,'allteamleaders.html',context)

def allmanagers(request):
    context={}
    m=Manager.objects.filter(is_active=True)
    print(m)
    context['managers']=m
    return render(request,'allmanagers.html',context)

def profile(request):
    return render(request,'profile.html')

def viewdetail(request,eid):
    e=Employee.objects.filter(id=eid)
    context={}
    context['employees']=e
    return render(request,'viewdetail.html',context)

def tl_viewdetail(request,eid):
    t=Teamleader.objects.filter(id=eid)
    context={}
    context['teamleaders']=t
    return render(request,'tl_viewdetail.html',context)

def m_viewdetail(request,eid):
    m=Manager.objects.filter(id=eid)
    context={}
    context['managers']=m
    return render(request,'m_viewdetail.html',context)

# def e_profile(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     profile = get_object_or_404(Employee, user=user)
#     return render(request, 'e_profile.html', {'profile': profile})