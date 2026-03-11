FROM cgr.dev/chainguard/node:latest-dev AS certbuilder

USER root
RUN apk add --no-cache ca-certificates

FROM cgr.dev/chainguard/node:latest

USER root

COPY --from=certbuilder /usr/bin/c_rehash /usr/bin/c_rehash
COPY --from=certbuilder /usr/sbin/update-ca-certificates /usr/sbin/
# COPY --from=certbuilder /usr/share/ca-certificates /usr/share/ca-certificates
COPY --from=certbuilder /etc/ca-certificates /etc/ca-certificates
COPY --from=certbuilder /etc/ssl/certs /etc/ssl/certs

RUN rm -f \
    /etc/ssl/certs/ca-certificates.crt \
    /etc/ssl/certs/ca-bundle.crt \
    /etc/ssl/certs/*.pem \
    /etc/ssl/certs/*.0

RUN mkdir -p \
    #     /etc/ssl/certs \
    /usr/share/ca-certificates \
    #     /usr/local/share/ca-certificates \
    && touch /etc/ssl/certs/ca-certificates.crt

USER 65532:65532

USER 65532:65532