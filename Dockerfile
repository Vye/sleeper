FROM centos:7

USER root

ENV APP_ROOT /app
ENV PORT 5000

# Sync project root to ${FLASK_ROOT}.
COPY api.py "${APP_ROOT}/api.py"

RUN \
    yum install -y epel-release && \
    yum install -y python36 python36-devel gcc python36-pip && \
    pip3 install responder

EXPOSE ${PORT}

WORKDIR ${APP_ROOT}


CMD ["bash", "-c", "exec /usr/bin/python3.6 api.py"]

