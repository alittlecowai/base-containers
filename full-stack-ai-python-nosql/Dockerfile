# ---
# --- Build running container (OS & Py packages)
# ---
# Reference uv image to get binaries
FROM ghcr.io/astral-sh/uv:latest AS uv_bin
FROM cgr.dev/chainguard/wolfi-base AS pybase
# Install and remove cache in 1 command to prevent scanner from detecting vuln files in this layer
RUN apk update \
    && apk add --no-cache \
    python-3.12 \
    ca-certificates \
    libreoffice\
    libmagic
# curl \

# Add `soffice` binary to PATH
ENV PATH="/usr/lib/libreoffice/program:$PATH"

# Python specific env
# flush logs to terminal immediately instead of buffering
ENV PYTHONUNBUFFERED=1
# don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Install uv and make uv available in PATH
COPY --from=uv_bin /uv /uvx /bin/

# Re-Create nonroot user with fixed UID/GID
RUN deluser nonroot && \
    delgroup nogroup && \
    addgroup --gid 49999 nonroot && \
    adduser -u 49999 -G nonroot -D -H nonroot

# Setup directory for nonroot
WORKDIR /app
RUN chown nonroot:nonroot /app

# Switch to 49999 (nonroot) for application-level setup. Must use number else k8s runAsNonRoot will error and complain non-numeric user
USER 49999

# copy pyproject and uv.lock first to use docker layer caching if these didnt change
COPY --chown=nonroot:nonroot pyproject.toml uv.lock ./
# install dependencies and clean cache in 1 command to prevent hidden files bloating image
ENV PATH="/app/.venv/bin:$PATH" \
    UV_NO_CACHE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=/usr/bin/python3 \
    VIRTUAL_ENV=/app/.venv
RUN uv sync --index-url https://pypi.org/simple
