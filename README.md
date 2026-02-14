# API Project Development Setup

This guide will help you set up and run the development environment for this API project.

## Prerequisites
- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/)
- [venv](https://docs.python.org/3/library/venv.html) for isolated environments
- [PostgreSQL](https://www.postgresql.org/) running and configured accordingly to conf/.env.dev dev settings

## 1. Clone the Repository
```bash
git clone <repository-url>
cd API
```

## 2. Create and Activate a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies
Install the main dependencies:
```bash
pip install -r requirements.txt
```
For development dependencies (testing, linting, etc.):
```bash
pip install -r requirements-dev.txt
```

## 4. Database Setup
Using Alembic for migrations:
- Run migrations:
```bash
export $(grep -v '^#' conf/.env.dev | xargs)
alembic upgrade head
```

## 5. Running the Application
To start the API (example using main.py):
```bash
python main.py
```
Or use your preferred ASGI/WSGI server (e.g., uvicorn, gunicorn) if applicable.

## 6. Running Tests
```bash
pytest test/
```

## 7. Linting and Formatting
```bash
flake8 .
black .
```

## 8. Useful Commands
- Run migrations: `alembic upgrade head`
- Create migration: `alembic revision --autogenerate -m "message"`
- Run tests: `pytest test/`

## 9. Additional Notes
- Update the database connection string as needed for your environment.
- See `doc/api.ipynb` for API documentation and usage examples.

---

For further questions, see the documentation in the `doc/` folder or contact the project maintainer.
