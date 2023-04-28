from crispy_forms.helper import FormHelper
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .files import LoginForm, NewUserForm, CreateTask
from django.contrib import messages
from .models import Task
from .files import TaskForm

# Create your views here.
@login_required()
def index(request):
    tasks = Task.objects.all().filter(user=request.user)
    return render(request, 'index.html', {'tasks':tasks})


def login_view(request):
    """
    If the request is a POST request, then we create a LoginForm object with the request and the POST
    data.
    If the form is valid, then we get the username and password from the form, authenticate the user,
    and log them in.
    If the request is not a POST request, then we create an empty LoginForm object.
    In either case, we render the login.html template with the form.

    :param request: The request object is passed to the view by Django. It contains all the information
    about the current request
    :return: The login_view function is returning a render function.
    """
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('taskly:dashboard')
    else:
        form = LoginForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


class LogoutView(generic.base.RedirectView):
    """
    It's a subclass of RedirectView that logs out the user and then redirects to the URL specified by
    the url attribute
    """
    url = reverse_lazy('taskly:index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('taskly:login')


def register(request):
    """
    If the request is a POST request, then validate the form and save the user. If the form is valid,
    then log the user in and redirect them to the login page. If the form is not valid, then display an
    error message. If the request is not a POST request, then display the form.

    :param request: The current request object
    :return: The form is being returned.
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("taskly:login")
        else:
            messages.error(request, "Unsuccessful Registration . Invalid information.")
    else:
        form = NewUserForm()

        # Use the Crispy Forms helper to add Bootstrap styling to the form
    form.helper = FormHelper()
    form.helper.form_class = 'form-group'
    form.helper.label_class = 'form-label'
    form.helper.field_class = 'form-control'
    return render(request=request, template_name="register.html", context={"register_form": form})





def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('taskly:dashboard')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'createTask.html', context)





@login_required(login_url='my_login')
def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'viewTask.html', context=context)


@login_required(login_url='my_login')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    # this allows us to work on the specific instance of the task (code below)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        # if the item is valid then we update the database

        if form.is_valid():
            form.save()
            # then we return the views tasks to see if our database is updated
            return redirect('taskly:view_task', pk=pk)
    else:
        form = TaskForm(instance=task)
    context = {'form': form, 'task': task}
    return render(request, 'updateTask.html', context=context)


# @login_required(login_url='my_login')
# def delete_task(request, pk):
#     # we are fetching our tasks from the database with the primary key
#     task = Task.objects.get(id=pk)
#     if request.method == 'POST':
#         # if selected operation then we delete
#         task.delete()
#         # if deleted then we would like to go to view task
#         return redirect('taskly:index')
#
#     context = {'task': task}
#     return render(request, 'deleteTask.html', context=context)



@login_required(login_url='my_login')
def delete_task(request, pk):
    # Fetching the task object from the database using the primary key
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # If the user confirms the deletion, then delete the task object
        task.delete()
        # Redirect to the viewTask page after deletion
        return redirect('taskly:dashboard')

    # Render the deleteTask.html template with the task object as context
    context = {'task': task}
    return render(request, 'deleteTask.html', context=context)
