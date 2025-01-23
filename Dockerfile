FROM python:3.12-slim

# Copy over app, reqs and env files
COPY src/ /app
COPY README.md /app
COPY pyproject.toml /app/pyproject.toml
COPY dist.env /app/.env
COPY entrypoint.sh /app/entrypoint.sh

# Set perms
RUN chmod +x /app/entrypoint.sh

# Set cwd to app
WORKDIR /app

# Setup package management
RUN apt-get update && apt-get install --no-install-suggests --no-install-recommends --yes pipx
ENV PATH="${PATH}:/root/.local/bin"
RUN pipx install poetry

# Install dependencies
RUN poetry install

# Setting up global app variables
ENV DB_CONFIG_PATH "config/databases.py"
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Run app
ENTRYPOINT [ "sh", "entrypoint.sh" ]

# Expose app to internet
EXPOSE 80
