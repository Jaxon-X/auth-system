# auth-system
# Django Rest Framework Authentication with JWT

This project implements user authentication using Django Rest Framework (DRF) and Simple JWT, with a custom login implementation.

## Features
✅ User Registration (Signup)  
✅ User Login with JWT (Custom Implementation)  
✅ Access & Refresh Token Mechanism  
✅ Token Refresh Endpoint  
✅ Secure API Authentication  

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # MacOS/Linux
   env\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### 🔹 Register a new user
**Endpoint:** `POST /user/api/register/`  
**Request Body:**
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "yourpassword"
}
```
**Response:**
```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com"
}
```

### 🔹 Login and obtain tokens (Custom Implementation)
**Endpoint:** `POST /user/api/login/`
**Request Body:**
```json
{
  "username": "testuser",
  "password": "yourpassword"
}
```
**Response:**
```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### 🔹 Refresh access token
**Endpoint:** `POST /user/api/token/refresh/`
**Request Body:**
```json
{
  "refresh": "your_refresh_token"
}
```
**Response:**
```json
{
  "access": "your_new_access_token"
}
```

### 🔹 Access a protected endpoint
Use the `access` token in the Authorization header:
```http
Authorization: Bearer your_access_token
```

---

## Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
```

---

## Contributing
Pull requests are welcome! Feel free to improve the authentication system or add new features. 🚀

---

## License
This project is licensed under the MIT License.


