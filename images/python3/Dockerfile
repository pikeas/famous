FROM aris/base:20150610
MAINTAINER Aris Pikeas <aris@pike.as>

RUN \
    apt-get update && \
    apt-get install -y \
        python3=3.4.3-1 \
        python3-dev=3.4.3-1 && \
    apt-get clean && rm -rf rm -rf /var/lib/{apt,dpkg} /tmp/* /var/tmp/*

# Ubuntu python package has broken ensurepip
COPY get-pip-7.0.3.py /tmp/get-pip.py
RUN \
    python3 /tmp/get-pip.py && \
    rm /tmp/get-pip.py

ENV PATH /root/.local/bin:$PATH
ENV PIP_USER 1
