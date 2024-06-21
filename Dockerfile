FROM registry.access.redhat.com/ubi9/ubi
RUN dnf install -y httpd /usr/bin/ps && \
    chown :root -R /run/httpd && \
    chmod -R g+rwX /run/httpd
ADD /rootfs /
EXPOSE 8080
LABEL io.openshift.min-cpu 2

CMD ["run-httpd"]

