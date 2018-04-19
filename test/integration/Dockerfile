FROM ubuntu:xenial

RUN apt-get update && \
  apt-get install -y python-pip python-dev && \
  pip install tox
WORKDIR /integration

CMD ["tox", "-e", "ui-tests"]