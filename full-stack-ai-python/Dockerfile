# Use wolfi-base to prevent CVEs as much as possible
FROM cgr.dev/chainguard/wolfi-base

# Recreate nonroot user with fixed UID/GID
RUN deluser nonroot
RUN delgroup nogroup
RUN addgroup -g 49999 nonroot
RUN adduser -u 49999 nonroot -G nonroot -D -s /bin/sh

# Install required packages
# gcc needed for pandas
RUN apk update && apk add uv gcc bash expat git curl libcurl-openssl4 wget openssh openssh-keyscan jq zip tzdata uuidgen gpg gpg-agent --no-cache

# Set timezone
SHELL ["/bin/bash", "-c"]
RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime
ENV TZ=Asia/Singapore

# Copy relevant application files
COPY pyproject.toml /usr/src/app/pyproject.toml
COPY uv.lock /usr/src/app/uv.lock

# Set permissions
RUN chown -R nonroot:nonroot /usr/src/app
RUN chown -R nonroot:nonroot /home/nonroot

# Final hardening to prevent privilege escalation before switching to non-root user
RUN find / -perm /6000 -type f -exec chmod a-s {} \; || true

# Remove sensitive files
RUN rm -rf /etc/ssh

# Set work directory
USER nonroot
WORKDIR /usr/src/app

# Install requirements via uv
ENV UV_COMPILE_BYTECODE=1
RUN uv sync --no-dev --locked

# Remove uv cache, prevent unused package vulnerabilities from appearing in container scan
RUN uv cache clean

# Set Python environment variables
ENV PATH="/usr/src/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
