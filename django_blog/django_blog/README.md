# Django Blog Project

This is a Django-based blog application focusing on issues affecting Nigeria, solutions to these issues, and challenges in the tech and ethical hacking industry in Nigeria. The project allows users to create, view, edit, and delete blog posts. It also includes user authentication features like registration, login, and profile management.

## Features

- **User Authentication**: 
  - User registration, login, and logout functionality.
  - Profile management (users can update their profiles).
  - Password hashing and security measures (e.g., CSRF protection).
  
- **Blog Post Management**:
  - CRUD (Create, Read, Update, Delete) operations for blog posts.
  - Blog posts can be categorized and filtered by author or category.
  - Text summarization and image generation (planned integration with third-party APIs).
  
- **Django REST Framework**:
  - APIs for interacting with blog posts (to create, update, delete, and view posts).
  
- **Front-end**:
  - Basic HTML and CSS for presentation.
  - Template rendering for views.
  
- **Database**:
  - MySQL database for storing user and blog post data.

## Installation
$bash; python -m venv venv
Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
Visit the application in your browser: http://127.0.0.1:8000/
### 1. Clone the Repository

```bash
git clone https://github.com/Ghostlyjeff/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django_blog


Deployment
You can deploy this project on platforms like Heroku or PythonAnywhere.

Deploying to Heroku
Create a Procfile and requirements.txt for Heroku.

Push the project to your Heroku Git repository.

Deploying to PythonAnywhere
Upload your project files to PythonAnywhere.

Set up a web app and configure the database.

Follow their guide to run Django on PythonAnywhere.

License
This project is licensed under the Alx License.

Contact
For any inquiries, feel free to reach out to [odifirijide1234@gmail.com].