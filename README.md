# Jahnon On Weels Project

This is a Django project that includes several files and directories. Below is a brief description of each file and its purpose.
The project was established for the company: Jahanon on wheels for order management.

## Instructions

This Django project is designed to provide a backend API for managing clients, products, orders, and order details. It allows you to perform various operations such as creating, updating, and deleting records. Additionally, it provides authentication and authorization mechanisms using JSON Web Tokens (JWT).

To run the Django project, please follow these instructions:

1. Ensure that you have Python installed on your system (preferably Python 3.6 or higher).

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database by applying migrations. Execute the following command:
    ```
    python manage.py migrate
    ```

4. Create a superuser account to access the admin interface by running:
    ```
    python manage.py createsuperuser
    ```

5. Start the development server with the following command:
    ```
    python manage.py runserver
    ```

6. You can now access the application at http://localhost:8000/.

## Technologies

This Django project utilizes the following technologies and frameworks:

* Django: A high-level Python web framework that provides a clean and pragmatic design for building web applications.

* Django REST framework: A powerful and flexible toolkit for building Web APIs.

* JSON Web Tokens (JWT): A standard method for representing claims securely between two parties using JSON objects.

* SQLite: A lightweight, serverless database engine that is included by default with Django.

* Django SimpleJWT: A library for JWT authentication in Django.

* Python: The programming language used to develop the project.

Please make sure you have a basic understanding of these technologies before working with the Django project.
