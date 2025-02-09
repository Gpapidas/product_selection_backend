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
   docker compose build
   ```
3. Start the application:
   ```bash
   docker compose up
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
