# Multi-User Todo Application Using Django

<img width="437" alt="image" src="https://github.com/user-attachments/assets/2b6a7310-364d-46b3-acbe-2c703b8ede00">


## Description
This project is a collaborative, multi-user todo application built using Django. It enables users to create, manage, and track their tasks, allowing them to work more effectively and stay organized.

## Features
- **User Registration & Authentication**: Allows secure user sign-up and login.
- **Task Management**: Users can create, edit, and delete tasks.
- **Task Assignment**: Assign tasks to specific users for better collaboration.
- **Status Tracking**: Mark tasks as completed or pending.
- **Task Filtering**: Filter tasks based on status, priority, and other criteria.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Err0r-By-Night/Todo_app_using_django.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Todo_app_using_django/todo
   ```
3. **Install dependencies**:
   ```bash
   pip install django
   ```
4. **Set up the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Open your browser** and go to [http://localhost:8000/](http://localhost:8000/).
2. **Register** as a new user or **log in** if you already have an account.
3. **Add, edit, and manage your tasks**.
4. **Collaborate** by assigning tasks to other users.

## Contributing

To contribute to this project:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make changes and commit**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature
   ```
5. **Submit a pull request**.

## About

This application enables users to independently manage tasks, plan their days, and collaborate effectively in a multi-user environment.

## Resources

- **Language Stack**: Python, HTML, CSS, JavaScript
