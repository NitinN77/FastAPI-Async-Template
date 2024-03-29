# FastAPI Async Template

- Asynchronous queries with asyncpg and SQLAlchemy 2.0
- Migrations using alembic
- An optimized dockerfile for production with gunicorn and reloadable uvicorn workers
- A compose file for a pleasant local development experience
- Poetry for dependency management
- Unit and Integration testing with pytest (async fixtures and async test support included)
- Code formatting with black and isort
- Type Checking with mypy
- Includes a simple logger

## Useful Commands

### Running the application

1. Make sure you have Docker installed on your local machine
2. From the root of the repository, run `docker compose up -d --build`
3. Open http://localhost:8000/docs to view the Swagger documentation

### Migrations

To work with migrations, make sure that you're in the directory of the root package (`cd src/fastapi_template`) and not in the root of the repository

1. Run `poetry install` and then `poetry shell` to activate the virtual environment
2. To generate migrations, run `alembic revision --autogenerate`. Check the generated migration file inside `src/fastapi_template/migrations/versions`
3. To apply migrations, run `alembic upgrade head`

### Testing

1. Make sure that the virtual environment is active by running `poetry shell`
2. To run unit tests, run `pytest .\tests\unit\`
3. To run integration tests, run `pytest .\tests\integration\`
4. To run all tests, run `pytest tests`

### Formatting and Type Checking

1. Make sure that the virtual environment is active by running `poetry shell`
2. To run black, run `black .`
3. To run isort, run `isort .`
4. To run mypy, run `mypy .`

## Folder Structure

#### `src`

- `dependencies/` FastAPI dependencies which are used by your routes. The database connection dependency is the most commonly used one. Learn more: https://fastapi.tiangolo.com/tutorial/dependencies/
- `handlers/` Route handler functions that are called by the routers when a request is received. The underlying business logic should be written here to avoid cluttering the router file. This is similar to the controller pattern in object-oriented projects
- `migrations/` Contains alembic configuration files and migration files generated by alembic
- `models/` Contains "model" classes used by SQLAlchemy. These classes represent a table from a relational database and lets us write clean ORM code using them
- `routers/` The routers (or subrouters) used by the FastAPI application. Should ideally be split by a router tag or prefix. For example: `logs.py` should contain all `/logs/*` routes
- `schemas/` Contains pydantic schemas used for request and response validation.
- `settings/` Contains the environment configuration and other settings if necessary
- `utils/` Utility functions which can be used by any other package. Global utilities such as loggers belong here
- `main.py` The entrypoint to the FastAPI application

#### `tests`

- `integration` Integration tests run using a test database (sqlite by default) and ensure queries are actually executed and return expected values. These can take quite some time to run depending on the queries inside your handler functions.
- `unit` Unit tests mock out all queries (and other 3rd party services) and only test 1st party logic in the handler functions. These run relatively quickly
