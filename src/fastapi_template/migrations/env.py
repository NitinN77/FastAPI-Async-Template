# !/bin/python3

from logging import getLogger
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from fastapi_template.settings.environment import get_settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


config.set_main_option("sqlalchemy.url", get_settings().DB_URL_FOR_MIGRATIONS)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from fastapi_template.models.base import Base

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


logger = getLogger("alembic")


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    try:
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                include_schemas=True,
            )

            with context.begin_transaction():
                context.run_migrations()
    finally:
        logger.info("Trying to close database connection... ")
        connection.close()
        logger.info(
            "Connection Status post closing connection: " "closed"
            if connection.closed
            else "open"
        )


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
