from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


# A list of url patterns.
app_name = "taskly"
urlpatterns = [
    # The default page that will be displayed when you go to the root of the website.
    path('', views.index, name='dashboard'),

    # An url for logging out, links in views and logout.html
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # An url for logging in, links in views and login.html
    path("login/", views.LoginView, name="login"),

    # An url for registering, links in views and register.html
    path('register/', views.register, name="register"),


    # Creating a path for the createTask function in views.py in order to create a task .
    path('create_task', views.create_task, name='create_task'),


    # Creating a path for the viewTask function in views.py in order to view task.
    path('view_task/<str:pk>/', views.view_task, name='view_task'),

    # Creating a path for the update_task function in views.py in order to update a task.
    path('update_task/<str:pk>/', views.update_task, name='update_task'),

    # A path for the deleteTask function in views.py in order to delete a task using the primary key.
    path('delete/<str:pk>/', views.delete_task, name='delete_task'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
