# 📝 TodoApp

**TodoApp** is a simple and extensible RESTful API built with Django and Django REST Framework that allows users to manage their tasks and to-do items. The project includes user authentication using JWT and provides endpoints for CRUD operations on todos.

---

## 🚀 Features

- ✅ User registration and authentication (JWT-based)
- 📝 Create, read, update, and delete todos
- 🔐 Protected routes for authenticated users
- 📦 Modular Django project structure
- 🔧 Configured for Docker and Docker Compose

---

## 🛠️ Built With

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [dj-rest-auth](https://github.com/jazzband/dj-rest-auth)

---

## 📦 Project Structure

TodoApp/
├── .github/ # GitHub actions and workflows
├── accounts/ # User registration, authentication
├── todos/ # Todo app logic
├── config/ # Project settings and URLs
├── manage.py
├── requirements.txt
└── docker-compose.yml


---

## ⚙️ Getting Started (Locally)

### 1. Clone the repository

```bash
git clone https://github.com/MahanMa78/TodoApp.git
cd TodoApp


# Create and activate virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt
python manage.py migrate

. . . 


🧪 TODOs and Improvements
 Add Swagger/OpenAPI documentation

 Add unit and integration tests

 CI/CD integration

 Frontend integration (optional)


🪪 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


📬 Contact
Built with ❤️ by @MahanMa78