# Task Manager 2

This is a simple task manager application built using Django.

## Installation

### Using venv

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/task-manager.git
    ```

2. Navigate to the project directory:

    ```
    cd task-manager
    ```

3. Create a virtual environment and activate it:

    ```
    python -m venv venv
    source venv/bin/activate    # On Windows, use: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Set up the database by running the following commands:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser account:

    ```
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```
    python manage.py runserver
    ```

8. Access the application by visiting http://localhost:8000 in your web browser.

### Using Docker

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/task-manager.git
    ```

2. Navigate to the project directory:

    ```
    cd task-manager
    ```

3. Build the Docker image:

    ```
    docker build -t task-manager-app .
    ```

4. Run the Docker container:

    ```
    docker run -d -p 8000:8000 --name task-manager-container task-manager-app
    ```

5. Access the application by visiting http://localhost:8000 in your web browser.

## Usage

The task manager allows you to create tasks and assign them to specific users. You can also mark tasks as completed and view a list of all tasks.

To create a task, log in as a superuser and navigate to the admin panel (http://localhost:8000/admin). From there, you can create new tasks and assign them to users.

To view all tasks, visit http://localhost:8000/tasks in your web browser.

## Secrets

Please note that this application requires certain secret configurations, such as database credentials and API keys, to function correctly. However, for security reasons, we do not include these secrets in the public repository.

To run the application, you will need to acquire and add these secrets yourself. Here's how:

1. Database Credentials:
   - Create a local settings file (e.g., `task_manager/local_settings.py`) in the project root.
   - Add your database credentials to this file using the same format as the main `settings.py`.
   - Ensure that this file is not included in version control by adding it to your `.gitignore` file.

2. API Keys:
   - If the application relies on any external APIs, obtain the necessary API keys from the respective providers.
   - Store these API keys securely in environment variables on your local machine.
   - Update the application code to read the API keys from environment variables.

By following these steps, you can keep your secrets safe and ensure that they are not exposed in public repositories.

## Credits

This application was created by Lehlohonolo Matlala. Feel free to fork the repository and make any changes you'd like.

