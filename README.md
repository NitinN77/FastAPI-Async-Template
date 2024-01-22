# FastAPI Template

- Asynchronous queries with asyncpg and SQLAlchemy 2.0
- Migrations using alembic
- An optimized dockerfile for production
- A compose file for a pleasant local development experience
- Poetry for dependency management

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
