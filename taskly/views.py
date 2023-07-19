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


def LoginView(request):
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



    
@login_required(login_url='my_login')
def create_task(request):
    """
    This function creates a new task for a logged-in user using a form and saves it to the database.

    :param request: The HTTP request object that contains information about the current request,
    including the user making the request, the HTTP method used (GET, POST, etc.), and any data
    submitted with the request
    :return: This function returns a rendered HTML template named 'createTask.html' with a context
    dictionary containing a TaskForm object. If the request method is POST and the form is valid, it
    creates a new task object with the user who made the request and redirects to the dashboard page.
    """
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
    """
    This is a Python function that requires login authentication to view a specific task and renders it
    on a web page.
    
    :param request: The HTTP request object that contains information about the current request, such as
    the user making the request, the HTTP method used, and any data submitted with the request
    :param pk: pk stands for "primary key" and is a unique identifier for a specific instance of a model
    in a database. In this case, it is used to retrieve a specific Task object from the database based
    on its primary key value
    :return: The view_task function is returning an HTTP response that renders the 'viewTask.html'
    template with the context dictionary containing the task object retrieved using the pk parameter.
    The function is decorated with the login_required decorator, which means that the user must be
    authenticated to access this view. If the user is not authenticated, they will be redirected to the
    'my_login' URL.
    """
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'viewTask.html', context=context)


@login_required(login_url='my_login')
def update_task(request, pk):
    """
    This function updates a task instance in the database and redirects to the view task page.
    
    :param request: The HTTP request object that contains information about the current request, such as
    the user making the request and any data submitted with the request
    :param pk: pk stands for "primary key" and is used to identify a specific instance of a model in the
    database. In this case, it is used to identify the specific task that needs to be updated
    :return: a rendered HTML template 'updateTask.html' with a context dictionary containing a form and
    a task object. If the request method is POST and the form is valid, the function redirects to the
    'view_task' view with the primary key of the updated task as a parameter.
    """
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


@login_required(login_url='my_login')
def delete_task(request, pk):
    """
    This function deletes a task object from the database and redirects to the dashboard page.
    
    :param request: The HTTP request object that contains information about the current request, such as
    the user making the request, the HTTP method used, and any data submitted with the request
    :param pk: pk stands for primary key, which is a unique identifier for each record in a database
    table. In this case, it is used to fetch the specific task object from the database that the user
    wants to delete
    :return: a rendered HTML template 'deleteTask.html' with the context of the task object. If the
    request method is POST, the function deletes the task object and redirects to the 'dashboard' page.
    """
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
