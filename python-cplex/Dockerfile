# check=skip=UndefinedVar
FROM ghcr.io/astral-sh/uv:latest AS uv_bin

FROM cgr.dev/chainguard/wolfi-base AS builder

RUN apk add --no-cache \
    python-3.12-dev \
    gcc

# Install uv and make uv available in PATH
COPY --from=uv_bin /uv /uvx /bin/

# Set working directory
WORKDIR /usr/src/app

# Configure Python and uv env
ENV PATH="/usr/src/app/.venv/bin:$PATH" \
    ## Flush logs to terminal immeidately without buffering
    PYTHONUNBUFFERED=1 \
    ## Don't write .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # Ensure uv does not create logs nor download Python
    UV_COMPILE_BYTECODE=1 \
    UV_NO_CACHE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=/usr/bin/python3 \
    VIRTUAL_ENV=/usr/src/app/.venv

# Copy requirements
COPY pyproject.toml uv.lock ./


# Install requirements via uv
RUN uv sync --no-dev --locked --index-url https://pypi.org/simple

# RUNTIME STAGE
FROM cgr.dev/chainguard/wolfi-base AS runtime

RUN apk add --no-cache \
    python-3.12 \
    libpq \
    libstdc++

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/.venv .venv

ENV PATH="/usr/src/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# # TEST STAGE (omitted for production build)
# FROM runtime AS test

# ARG CI=true

# RUN if [ "$CI" != "true" ]; then \
#     echo "Running cplex locally" \
#     # Install cplex
#     COPY cplex ./cplex \
#     RUN docplex config --upgrade ./cplex \
#     # Run sample code
#     COPY solve.py . \
#     python solve.py \
#     else \
#     echo "Skipping tests in CI"; \
#     fi
