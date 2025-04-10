# 📝 Blog Clone Project (Django)

A fully functional Blog Clone Project built with Django, featuring user authentication, post creation, editing, deletion, and commenting functionalities.

Perfect for learning how to build a dynamic web application using Django's powerful tools.



## 🚀 Features

🧩 User Registration & Login/Logout



📝 Create, Read, Update, and Delete (CRUD) blog posts



💬 Add comments to posts



🏷️ Categorize posts by tags or topics



🧑‍💻 Admin dashboard for managing content



🖼️ Image upload for blog posts



📅 Post timestamp and author attribution



📂 Responsive design with Bootstrap (if you used it)



## 🛠️ Tech Stack

Backend: Django, Python



Database: SQLite (by default), can be upgraded to PostgreSQL



Frontend: Django Templates, Bootstrap / CSS



Authentication: Django’s built-in authentication system



## 📂 Project Structure



/blog_clone_project

│── manage.py

│── /blog

│     │── models.py

│     │── views.py

│     │── urls.py

│     │── templates/

│     │── static/

│     │── forms.py

│     │── admin.py

│── /blog_clone_project

│     │── settings.py

│     │── urls.py

│     │── wsgi.py

│── /media

│── requirements.txt

│── README.md

## ⚙️ Installation

### 1️⃣ Clone the repository



git clone https://github.com/abhinav744/Blog-Clone-Project-Django.git

cd Blog-Clone-Project-Django

### 2️⃣ Set up virtual environment



python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3️⃣ Install dependencies



pip install -r requirements.txt

### 4️⃣ Apply migrations



python manage.py makemigrations

python manage.py migrate

### 5️⃣ Create superuser



python manage.py createsuperuser

### 6️⃣ Run the development server



python manage.py runserver

Visit: http://127.0.0.1:8000/



## 🧩 Features Breakdown

Feature	Description

Authentication	Register, Login, Logout

Post Management	CRUD operations on blog posts

Comments	Commenting system for user engagement

Admin Panel	Manage posts and users via Django admin

Media Uploads	Upload and display images with posts

## 📦 Requirements

Python 3.x



Django 4.x



Pillow (for image processing)





## 🤝 Contributing

Contributions are welcome!

If you have suggestions or improvements, feel free to fork this repository and submit a pull request.




