# Todo App with Django Templates and Basic Authentication

This is a **Todo App** built using **Django** with a simple HTML interface for managing tasks. It uses **Django templates** for rendering the UI and **basic authentication** to secure the user login and registration. Users need to log in to create, view, update, and delete their own todos. 

## Features

1. **User Authentication:**
   - Users can **register**, **log in**, and **log out** using the provided endpoints.
   - Passwords are securely stored using Django’s built-in `User` model.
   - Authentication is done using **basic Django session-based authentication**, without any token-based authentication like JWT.
   
2. **Todo CRUD Features:**
   - Users can **Create**, **Read**, **Update**, and **Delete** their own todos.
   - Each user has access only to their own todos, ensuring privacy and security.

3. **Django Templates:**
   - The app uses **Django templates** to render the user interface.
   - The interface is minimal, with no advanced styling (no CSS or JavaScript).
   - Users can view, create, update, and delete tasks through simple HTML forms.

## Endpoints and Views

### Authentication

1. **Register:**
   - **POST** `/register/` - Register a new user.
   - Uses Django's `UserCreationForm` to register users and automatically logs them in after successful registration.

2. **Login:**
   - **POST** `/login/` - Login an existing user.
   - Upon successful login, users are redirected to the Todo list view.

3. **Logout:**
   - **POST** `/logout/` - Logs the user out and redirects them to the login page.

### Todo Management (Requires Authentication)

1. **Get Todo List:**
   - **GET** `/` - Displays the todo list for the authenticated user. This is the home page of the application.
   - Users can also search for specific tasks by title.

2. **View Todo Details:**
   - **GET** `/todo/<int:pk>/` - Displays the details of a specific todo.

3. **Create Todo:**
   - **GET/POST** `/todo/create/` - Allows the user to create a new todo.

4. **Update Todo:**
   - **GET/POST** `/todo/update/<int:pk>/` - Allows the user to update an existing todo.

5. **Delete Todo:**
   - **POST** `/todo/delete/<int:pk>/` - Deletes a specific todo.

## How It Works

### 1. User Registration and Login
- A user can register through the `/register/` endpoint, which uses Django’s built-in `UserCreationForm` to create a new user.
- After successful registration, the user is automatically logged in and redirected to the todo list view.
- The login system uses **basic Django authentication**. Once logged in, the user can view their todos and perform CRUD operations.

### 2. Todo CRUD Operations
- **Create**: Users can create a new task through a simple HTML form. Once submitted, the task will be added to their todo list.
- **Read**: The todo list view shows all the tasks that belong to the logged-in user. There is a simple search function that allows users to filter tasks by title.
- **Update**: Users can update a task by selecting it from the todo list and editing the task details in a form.
- **Delete**: Users can delete a task, and it will be removed from their todo list.

### 3. Django Templates and Forms
- The HTML interface is rendered using **Django templates**. Basic Django forms are used to handle user inputs, such as registering users, logging in, and creating/updating/deleting tasks.
- Each view is associated with a template that renders the corresponding page, making it easy to customize and extend the user interface if needed.

How to Run the App

1.	Clone the repository to your local machine:
  ```bash
  git clone <repository-url>
  ```
2. Set up the virtual environment and install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the database migrations:
  ```bash
  python manage.py migrate
  ```
4. Create a superuser to access the Django admin panel:
  ```bash
  python manage.py createsuperuser
  ```
5. Run the development server:
  ```bash
  python manage.py runserver
  ```
6. Access the app at http://127.0.0.1:8000/

## Requirements
- Python 3.x
- Django 4.x or higher
- Other dependencies listed in requirements.txt
