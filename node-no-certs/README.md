# About

This creates a node image that has `ca-certificate` package installed, but with all ca certificates removed. In other words, it does not trust any domain and must have new certificates installed with `update-ca-certificate` before it can install packages from any repository.

## Set-up for testing

### Create a test cert:

##### Windows powershell

```
openssl req -x509 -newkey rsa:2048 -days 365 -nodes `
  -keyout test.key `
  -out test.crt `
  -subj "/CN=Test CA"
```

### Build docker image

```
docker build -t node-no-certs .
```

## Testing

### No trust

```
docker run --rm --entrypoint sh node-no-certs -c "ls /etc/ssl/certs"
```

##### Expected output:

```
<none>
```

### Certificate installation

```
docker run --rm --user root --entrypoint sh `
    -v "${PWD}/test.crt:/usr/local/share/ca-certificates/test.crt" `
    -v "${PWD}/test.js:/test.js" `
    node-no-certs `
    -c 'ls -l /etc/ssl/certs/ca-certificates.crt; update-ca-certificates; ls -l /etc/ssl/certs/ca-certificates.crt'
```

##### Expected output:

```
-rw-r--r--      1 root      root        0       Mar 11 07:52 /etc/ssl/certs/ca-certificates.crt
-rw-r--r--      1 root      root        1127    Mar 11 07:57 /etc/ssl/certs/ca-certificates.crt
```
