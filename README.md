# Product Selection Backend

## How to Run (with Docker - Recommended)

### Prerequisites
- Rename `.env.template` to `.env` or create a new `.env` file and copy the contents of `.env.template` inside.
- Install Docker ([Get Docker](https://docs.docker.com/get-docker/)).

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd product_selection_backend
   ```
2. Build the containers:
   ```bash
   docker compose -f development.yaml build
   ```
3. Start the application:
   ```bash
   docker compose -f development.yaml up
   ```

The backend should now be running at `http://127.0.0.1:8000`.


## How to Run (Without Docker)

### Prerequisites
- Rename `.env.template` to `.env` or create a new `.env` file and copy the contents of `.env.template` inside.
- Install Python (preferably **3.12+**).
- Install Pip.
- (Optional) Use a virtual environment: `venv`, `conda`, `pipenv`, `poetry`, etc.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd product_selection_backend
   ```
2. Install dependencies:
   ```bash
   pip install -r development.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the application:
   ```bash
   python manage.py runserver
   ```

The backend should now be running at `http://127.0.0.1:8000`.

---

## Entering the container
If you are running the application using Docker you can enter the container to run management commands by executing:
```bash
docker exec -it product_selection_backend-web-1 /bin/bash
```
or you can navigate through the Docker Desktop application to the container

---

## Database Setup & Migrations

### Running Migrations
If this is your first time running the project, apply database migrations by executing:

```bash
python manage.py migrate
```

### Creating a Superuser
To create a superuser for Django Admin, run:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

---

## Data Seeding

The system provides **data seeding** for easier development and testing.

### Seed Data
If you want to seed data you can run:
```bash
python manage.py seeds
```

### Seed Test Data
Test Data are automatically seeded when you are running tests, the command that runs is:

```bash
python manage.py test_seeds
```

---

## Running Tests
To run all tests:

```bash
python manage.py test
```
---
## Testing Infrastructure

We use a **custom test runner** (`shared/tests/runner.py`) that seeds a **test database** before running tests.  
The base test setup is in **`shared/tests/base.py`**, where:

- The test database is pre-seeded.
- Test users are set up automatically.
- JWT tokens are generated dynamically for authentication.
- Utility methods like `authenticate()` and `unauthenticate()` are provided.

---

## Settings Structure

Instead of a single `settings.py` file, we use a **modular settings structure**:

- `settings/base.py` → Contains core settings used across all environments.
- `settings/local.py` → Used for local development.
- `settings/production.py` → Used in production.
- `settings/global_settings.py` → Stores global variables used throughout the application.

Each environment loads the respective settings file dynamically.

---

## Database Connection for External Tools

If you need to connect a **Database Management Tool** (e.g., **DBeaver, TablePlus**), use the following credentials (found in `compose.yaml`):

| Parameter         | Value |
|------------------|-------|
| **Host**        | `127.0.0.1` |
| **Port**        | `5432` |
| **Database**    | `product_selection_db` |
| **User**        | `product_selection_user` |
| **Password**    | `product_selection_password` |

---

## API Documentation

We use **drf-spectacular** to generate API documentation.

Once the application is running, you can access:
- **Swagger UI**: [`http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/api/schema/swagger-ui/)
- **Redoc**: [`http://127.0.0.1:8000/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/)
- **Raw OpenAPI Schema**: [`http://127.0.0.1:8000/api/schema/`](http://127.0.0.1:8000/api/schema/)

---

## Django Admin

The **Django Admin Panel** is accessible at:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Login with the credentials created in **Creating a Superuser**.

---

## Technologies Used

- **Django** 5.1.6 (with Django REST Framework)
- **PostgreSQL** (via Docker, using `psycopg2-binary` 2.9.10)
- **Docker & Docker Compose**
- **JWT (JSON Web Token) Authentication** (using `djangorestframework-simplejwt` 5.4.0)
- **drf-spectacular** 0.28.0 (API documentation)
- **drf-standardized-errors** 0.14.1 (standardized API error handling)
- **django-filter** 24.3 (for advanced filtering in DRF)
- **python-dotenv** 1.0.1 (for environment variable management)
- **Testing & Code Quality:**
  - **Django TestCase** (built-in Django testing framework)
  - **pip-audit** 2.7.3 (security audit for dependencies)
  - **bandit** 1.8.2 (security linting for Python code)
  - **pylint** (static code analysis)
  - **black** 25.1.0 (code formatting)
  - **nplusone** 1.0.0 (detecting N+1 query problems)
  - **django-extensions** 3.2.3 (additional management commands)
