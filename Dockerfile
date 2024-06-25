FROM registry.access.redhat.com/ubi9/python-39
COPY app.py /opt/app-root/src
CMD [ "/usr/libexec/s2i/run" ]
