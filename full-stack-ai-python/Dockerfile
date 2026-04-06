# BASE STAGE
FROM ghcr.io/astral-sh/uv:latest AS uv_bin

# BUILDER STAGE
FROM cgr.dev/chainguard/wolfi-base AS builder

# Install apk packages
RUN apk add --no-cache \
    python-3.12-dev \
    gcc

# Install uv and make uv available in PATH
COPY --from=uv_bin /uv /uvx /bin/

# Set working directory
WORKDIR /usr/src/app

# Copy relevant application files
COPY pyproject.toml /usr/src/app/pyproject.toml
COPY uv.lock /usr/src/app/uv.lock

# Prevent uv from downloading standalone python
ENV UV_PYTHON_INSTALL=0

# Install requirements via uv
ENV UV_COMPILE_BYTECODE=1
RUN uv sync --no-dev --locked

# Remove uv cache, prevent unused package vulnerabilities from appearing in container scan
RUN uv cache clean

# RUNTIME STAGE
FROM cgr.dev/chainguard/wolfi-base AS runtime

# Install apk packages
RUN apk add --no-cache \
    python-3.12 \
    tzdata

# Recreate nonroot user with fixed UID/GID
RUN deluser nonroot
RUN delgroup nogroup
RUN addgroup -g 49999 nonroot
RUN adduser -u 49999 nonroot -G nonroot -D -s /bin/sh

# Set timezone
ENV TZ=Asia/Singapore
RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime

# Set permissions
WORKDIR /usr/src/app
RUN chown -R nonroot:nonroot /usr/src/app
RUN chown -R nonroot:nonroot /home/nonroot

# Final hardening to prevent privilege escalation before switching to non-root user
RUN find / -perm /6000 -type f -exec chmod a-s {} \; || true

# Remove sensitive files
RUN rm -rf /etc/ssh

# Set working directory
USER nonroot

COPY --from=builder /usr/src/app/.venv .venv

ENV PATH="/usr/src/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
