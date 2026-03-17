# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/wolfi-base:latest AS barman-builder

USER root

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    gcc \
    python3-dev \
    postgresql-dev

# Install Barman and common cloud dependencies.
# boto3 is needed for AWS-backed object store workflows.
RUN python3 -m pip install --no-cache-dir --prefix=/install \
    "barman>=3.14,<4" \
    "boto3>=1.29"

RUN echo "debug" && python3 -c "import site; print(site.getsitepackages())"

FROM cgr.dev/chainguard/postgres:latest

USER root

COPY --from=barman-builder /usr/bin/python3 /usr/bin/python3
COPY --from=barman-builder /usr/lib/ /usr/lib/
COPY --from=barman-builder /install/lib/python3.13/site-packages/ /usr/lib/python3.13/site-packages/
COPY --from=barman-builder /install/bin/ /usr/local/bin/

ENV PATH="/usr/local/bin:${PATH}"

# Add postgres user/group entries for UID/GID 26 if missing
RUN grep -q '^postgres:x:26:' /etc/group || echo 'postgres:x:26:' >> /etc/group && \
    grep -q '^postgres:x:26:26:' /etc/passwd || echo 'postgres:x:26:26:PostgreSQL:/var/lib/postgresql:/sbin/nologin' >> /etc/passwd && \
    mkdir -p /var/lib/postgresql /controller && \
    chown -R 26:26 /var/lib/postgresql /controller

USER 26