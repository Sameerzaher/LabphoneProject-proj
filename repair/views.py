from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import RepairForm
from .models import Repair
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerForm(request):
    if (request.method == 'GET'):
        return render(request, 'Repair/register.html', {'form': UserCreationForm() })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('UserDashboard')
            except IntegrityError:
                return render(request, 'Repair/register.html', {'form': UserCreationForm(), "errMsg": "User exists. Choose a different one" })
        else:
            # print('Error message - type mismatch')
            return render(request, 'Repair/register.html', {'form': UserCreationForm(),  "errMsg": "Password didn't match" })

def myRepairs(request):
    Repairs=Repair.objects.filter(user_id=request.user)
    return render(request, 'Repair/myRepairs.html', {'allrepairs': Repairs})

def UserDashboard(request):
    Repairs=Repair.objects.filter(user_id=request.user)
    return render(request, 'Repair/UserDashboard.html', {'allrepairs': Repairs})
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')

    return render(request, 'Repair/AdminDashboard.html')
def commonBugs(request):
    Repairs=Repair.objects.filter(user_id=request.user)
    return render(request, 'Repair/commonBugs.html', {'allrepairs': Repairs})

        
def loginuser(request):

    if (request.method == 'GET'):
        return render(request, 'Repair/loginform.html', {'form': AuthenticationForm() })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'Repair/loginform.html', {'form': AuthenticationForm(), "errMsg": "User doesn't exist" })   
        else :
            login(request, user)
            return redirect('UserDashboard') 

def homepage(request):
    return render(request, 'Repair/index.html')
# CRUD
@login_required
def createNewRepair(request):
    if request.method == 'GET':
        return render(request, 'Repair/createnewRepair.html', {'form': RepairForm() })
    else:
        # pass
        try:
            form = RepairForm(request.POST)
            newRepair = form.save(commit=False)
            newRepair.user_id = request.user
            newRepair.save()
            return redirect('UserDashboard')
        except ValueError:
            return render(request, 'Repair/createnewRepair.html', {'form': RepairForm(), 'errMsg': 'Data mismatch'})

@login_required
def updateRepair(request, Repair_pk):

    repair = get_object_or_404(Repair, pk=Repair_pk, user_id=request.user)

    if (request.method == 'GET'):
        form = RepairForm(instance=repair)
        return render(request, 'Repair/updateRepair.html', {'repair': repair, 'form': form})
    else:
        try:
            form = RepairForm(request.POST, instance=repair)
            form.save()
            return redirect('myRepairs')
        except ValueError:
            return render(request, 'Repair/updateRepair.html', {'form': form, 'errMsg': "Data mismatch"})
   
@login_required
def doneRepair(request, Repair_pk):
    repair = get_object_or_404(Repair, pk=Repair_pk, user_id=request.user)

    if (request.method == 'POST'):
        Repair.dateCompleted = timezone.now()
        repair.save()
        return redirect('myRepairs')

@login_required
def deleteRepair(request, Repair_pk):
    repair = get_object_or_404(Repair, pk=Repair_pk, user_id=request.user)

    if (request.method == 'POST'):
        repair.delete()
        return redirect('myRepairs') 


