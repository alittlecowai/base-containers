FROM mongodb/mongodb-community-search:0.60.1

# Update all OS packages and clear cache to keep the image small
# Amazon Linux 2 uses yum; Amazon Linux 2023 uses dnf
RUN yum update -y --releasever=latest && \
    yum clean all && \
    rm -rf /var/cache/yum
