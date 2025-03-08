# User Management System API

This project is a Django REST Framework (DRF) based API that handles user authentication, registration, profile management, and password updates. It's designed to help you understand key DRF concepts like serializers, views, and authentication.

---

## 🚀 Features
✅ User Registration with Token Authentication  
✅ User Login with Token Generation  
✅ User Profile Management  
✅ Secure Logout Functionality  
✅ Password Change API for Logged-in Users  

---

## 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/darkflayer/Learning-Python.git
cd Learning-Python
```

2. **Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Mac/Linux
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a Superuser (For Admin Access)**
```bash
python manage.py createsuperuser
```

6. **Start the Development Server**
```bash
python manage.py runserver
```

---

## 📋 API Endpoints

### 🔐 **Authentication**
| Endpoint                  | Method | Description                        |
|--------------------------|---------|------------------------------------|
| `/api/users/register/`    | POST     | Register a new user               |
| `/api/users/login/`       | POST     | Log in and get a token             |
| `/api/users/logout/`      | POST     | Log out and destroy token          |
| `/api/users/profile/`     | GET      | Get logged-in user's profile data  |
| `/api/users/change-password/` | POST | Change password for logged-in users |

---

## 🧪 Testing API with Postman
1. Open **Postman**.  
2. For protected endpoints, add the following in the **Headers** tab:  
```
Authorization: Token <YOUR_TOKEN>
```
3. Use appropriate request types (**POST**, **GET**, etc.) with sample data to test the endpoints.

---

## 🧑‍💻 Project Structure
```
Learning-Python/
├── users/
│   ├── migrations/
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
├── myapi/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🤝 Contribution
Contributions are welcome! Feel free to fork the repo and submit pull requests. If you encounter any issues, create an issue in the repository.

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For queries, feel free to reach out via GitHub Issues or email at **your_email@example.com**. 😊

