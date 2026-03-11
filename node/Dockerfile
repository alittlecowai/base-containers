FROM cgr.dev/chainguard/node:latest AS base

USER root
RUN apk add --no-cache ca-certificates

# Switch back to non-root user defined by chainguard node base image
USER 65532:65532