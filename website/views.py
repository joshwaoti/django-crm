from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):

    records = Record.objects.all()
    # user = request.user
    
        #Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')

        else:
            messages.error(request, "There was an error trying to log you in, try again ...")
            return render(request, 'home.html', {})
    user = request.user
    context = {
          'records': records,
          'user' : user,
    }
    

    return render(request, 'home.html', context)



def logout_user(request):
        logout(request)
        messages.success(request, "You have been logged out")

        return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
     


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)

    else:
        messages.warning(request, 'You are not logged in')
        return redirect('home')
      
    return render(request, 'record.html', context = {
            'customer_record' : customer_record,
      })

def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, "You have deleted record successfully")
        return redirect('home')

    else:
         messages.warning(request, 'You must be logged in to delete record')
         return redirect('home')



def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record updated successfully")
                return redirect('home')
                print(add_record)
            
        return render(request, 'add_record.html', {'form': form})

    else:
        messages.success(request, "You must be logged in")
        return redirect('home')   



    return render(request, 'add_record.html', context={
          'form':form,
     })


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('home')

        return render(request, 'update_record.html', {'form': form})

    else:
        messages.success(request, "You must be logged in")
        return redirect('home')