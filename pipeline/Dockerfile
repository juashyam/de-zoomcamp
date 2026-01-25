# Start with slim Python 3.13 image
FROM python:3.13-slim

# Copy uv binary from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /var/www/html/pipeline

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/var/www/html/pipeline/.venv/bin:$PATH"

# Copy dependency files first 
COPY pyproject.toml .python-version uv.lock ./
# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy application code
COPY pipeline.py ./

# Set entry point
# ENTRYPOINT ["uv", "run", "pipeline.py"]
# With ENV PATH, we don't need to specify uv explicitly
ENTRYPOINT ["python", "pipeline.py"]