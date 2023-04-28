# Task-Manager-2

This is a simple task manager application built using Django.

## Installation

    Clone the repository to your local machine:
    
git clone https://github.com/your-username/task-manager.git

    Install the required dependencies:

pip install -r requirements.txt

    Set up the database by running the following commands:

python manage.py makemigrations
python manage.py migrate

    Create a superuser account:

python manage.py createsuperuser

    Run the development server:

    python manage.py runserver

    Access the application by visiting http://localhost:8000 in your web browser.

## Usage

The task manager allows you to create tasks and assign them to specific users. You can also mark tasks as completed and view a list of all tasks.

To create a task, log in as a superuser and navigate to the admin panel (http://localhost:8000/admin). From there, you can create new tasks and assign them to users.

To view all tasks, visit http://localhost:8000/tasks in your web browser.
Credits

This application was created by Your Name. Feel free to fork the repository and make any changes you'd like.
