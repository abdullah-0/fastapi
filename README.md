🚀 FastAPI Boilerplate
======================

A clean, extensible, and production-ready FastAPI boilerplate designed for building scalable backend APIs.

✅ Features
-----------

- 🔐 JWT Authentication with refresh tokens
- 👤 Generic User APIs
  - Register
  - Login
  - Refresh
  - Get current user (/me)
- 📝 Full CRUD for a sample `Entity` model (with authentication)
- 🐘 PostgreSQL 17 via Docker
- 📄 Auto-generated OpenAPI docs at /docs
- 🧪 Alembic for database migrations
- 🧹 Code formatted using Black
- 🐳 Dockerized for easy local development and deployment
- 📂 Includes `deploy/` folder with systemd service and Nginx config

⚙️ Requirements
---------------

- Python 3.10+
- Docker + Docker Compose

🐳 Docker Setup (Recommended)
-----------------------------

### Clone or fork this repository
```
git clone https://github.com/abdullah-0/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### Start the containers
```
docker-compose up --build
```
🔧 Local Development Setup
--------------------------

### Install dependencies

```
pip install -r requirements.txt
```
### Run Alembic migrations
```
alembic revision --autogenerate -m "initial"
alembic upgrade head
```
### Format code (optional)
```
black .
```

📂 Deployment
-------------

The `deploy/` folder includes:

- fastapi.service — systemd service file for running the app
- nginx.conf — sample Nginx configuration

📫 API Docs
-----------

Once the server is running, navigate to:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

📝 License
----------

Public License (WTFPL)

You can do anything with this code.

If you like it Give it a Star.
