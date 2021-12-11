from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm  ,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from todoList.models import Task
from todoList.forms import todoform
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_user')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = todoform()
        todos = Task.objects.filter(user=user)
        context ={
            'form':form,
            'todos':todos
        }
        return render(request,'todoList/index.html',context)
    else:
        form = todoform()
        context ={
            'form':form,
        }
        return render(request,'todoList/index.html',context)

    
def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context ={
            'form':form
        }
        return render(request,'todoList/login.html',context) 
    else:
        form = AuthenticationForm(data=request.POST)
        context ={
            'form':form
        }
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login_user')    
        else:
            return render(request,'todoList/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login_user')


def signup_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request,'todoList/signup.html',context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login_user')
            else:
                return redirect("signup_user")
        else:
            return render(request,'todoList/signup.html',context)


@login_required(login_url='login_user')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        # print(user)
        form =todoform(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            # print(todo)
            # print(form.cleaned_data)
            return redirect('home')

        else:
            return render(request,'todoList/index.html',context)

    else:
        return redirect('login_user')        

@login_required(login_url='login_user')
def delete_todo(request,id):
    todo = Task.objects.get(id=id)
    todo.delete()
    return redirect('home')

@login_required(login_url='login_user')
def edit_todo(request,id):
    if request.method =='GET':
        form = todoform()
        # print(request.GET)
        context ={
            'form':form,
            'id':id
        }
        return render(request,'todoList/edit.html',context)
    else:
        todo = Task.objects.get(id=id)
        todo.title = request.POST['title']
        todo.status = request.POST['status']
        todo.priority = request.POST['priority']
        todo.save()
        return redirect('home')




            


         


