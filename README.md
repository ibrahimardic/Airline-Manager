
# Airline Manager

A Django-based application for managing airline operations, including airlines, aircraft, and user authentication. This project follows the Django Rest Framework (DRF) architecture to build and expose REST APIs, enabling efficient airline and user management.

## Features

* **JWT Authentication:** Secure login and registration using JSON Web Tokens (JWT).
* **Airline and Aircraft Management:** CRUD operations for airlines and aircraft.
* **Docker Support:** Docker configuration for containerized deployment.
* **CI/CD Integration:** GitHub workflows for automated testing and deployment.
* **SQLite Database:** Default database for quick prototyping.
* **Comprehensive Tests:** Test cases for CRUD operations and authentication endpoints.

## Project Structure


```
Airline-Manager/
│
├── AirlineManager/              # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Django project settings
│   ├── urls.py
│   └── wsgi.py
│
├── airlines/                    # Airlines application
│   ├── api/                     # API views and serializers
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── models.py                # Data models for airlines and aircraft
│   ├── admin.py
│   └── tests.py
│
├── users/                       # User management application
│   ├── api/
│   │   ├── urls.py
│   │   └── views.py
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   └── views.py
│
├── tests/                       # Test cases for endpoints
│   ├── Airline_Crud_Operations.json
│   └── Authentication_endpoints.json
│
├── .github/                     # CI/CD workflows
│   └── workflows/
│       ├── build-and-deploy.yml
│       └── build-without-docker.yml
│
├── dockerfile                   # Docker configuration file
├── manage.py                    # Django management script
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # SQLite database file
└── .gitignore                   # Files to ignore in Git

```

## Setup and Installation


1. **Clone the repository:**
```
git clone https://github.com/ibrahimardic/Airline-Manager.git
cd Airline-Manager
```

2. **Set up a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows, `venv\Scripts\activate`
```

3. **Install dependencies:**
```
pip install -r requirements.txt
```

4. **Run migrations:**
```
python manage.py migrate
```

5. **Start the development server:**
```
python manage.py runserver
```

6. **Access the application:**
```
Open your browser and go to http://127.0.0.1:8000
```
## API Usage

#### Airlines Endpoints

List all airlines and create new airline.

```http
  GET /airline/
  POST /airline/
```

```http
  GET /airline/{pk}/
  PATCH /airline/{pk}/
  DELETE /airline/{pk}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pk`      | `string` | **Required**. Airline's id |


#### Aircrafts Endpoints
List all aircrafts and create new aircraft. (Airline reference is required to create new aircraft)
```http
  GET /aircraft/
  POST /aircraft/
```

```http
  GET /aircraft/{pk}/
  PATCH /aircraft/{pk}/
  DELETE /aircraft/{pk}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pk`      | `string` | **Required**. Aircraft's id |
  

#### User Authentication Endpoints

```http
  POST /api/register/

  ```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username |
| `password`      | `string` | **Required**. Password |
| `email`      | `string` | **Required**. Email address |

```http
  POST /api/login/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username |
| `password`      | `string` | **Required**. Password |

```http
  POST /api/logout/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `refresh`      | `string` | **Required**. Refresh token to successfully logout |

## CI/CD Pipeline

* The project uses **GitHub Actions** for continuous integration and deployment.
* Workflows available:
    * **build-and-deploy.yml:** Deploys the Dockerized project to an AWS EC2 instance. (Main workflow)
    * **build-without-docker.yml:** Runs tests and builds without Docker.

## Deployment

You can deploy this application using **Docker:**

1. **Build the Docker image:**

```
docker build -t airline-manager .
```
2. **Run the Docker container:**
```
docker run -d -p 8000:8000 airline-manager
```
Access the application at http://localhost:8000/.