# etl-saas-platform

API-first ETL SaaS Platform for transferring data between databases.

Built with FastAPI, SQLAlchemy, PostgreSQL, and JWT-based authentication with role-based access control (RBAC).

## Requirements

- Python 3.11+
- PostgreSQL 13+

## Setup

### 1. Clone and install dependencies

```bash
git clone https://github.com/danyel66/etl-saas-platform.git
cd etl-saas-platform
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your database credentials and a strong SECRET_KEY
```

| Variable            | Description                         | Default        |
|---------------------|-------------------------------------|----------------|
| `POSTGRES_USER`     | PostgreSQL username                 | `postgres`     |
| `POSTGRES_PASSWORD` | PostgreSQL password                 | —              |
| `POSTGRES_DB`       | Database name                       | `etl_saas_db`  |
| `POSTGRES_HOST`     | Database host                       | `localhost`    |
| `POSTGRES_PORT`     | Database port                       | `5432`         |
| `SECRET_KEY`        | Secret key for JWT signing          | —              |
| `DATABASE_URL`      | Full DB URL (overrides above vars)  | —              |

### 3. Run database migrations

```bash
alembic upgrade head
```

### 4. Start the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## API Endpoints

| Method | Path              | Auth     | Description                  |
|--------|-------------------|----------|------------------------------|
| POST   | `/signup/`        | None     | Register a new user          |
| POST   | `/login/`         | None     | Obtain a JWT access token    |
| GET    | `/me`             | Bearer   | Get current user profile     |
| GET    | `/protected-data` | Bearer   | Access protected resource    |
| GET    | `/admin-only`     | Bearer   | Admin-only endpoint          |

## Running Tests

```bash
pip install pytest pytest-cov httpx
pytest tests/ -v --cov=app
```

Tests use an in-memory SQLite database — no PostgreSQL required.

## Project Structure

```
app/
├── main.py            # FastAPI app, routes
├── database.py        # SQLAlchemy engine, session, get_db
├── utils.py           # Password hashing, JWT utilities
├── models/user.py     # SQLAlchemy User model
├── schemas/user.py    # Pydantic request/response schemas
└── dependencies/
    └── auth.py        # get_current_user, require_role dependencies
alembic/               # Database migrations
tests/                 # pytest test suite
```
