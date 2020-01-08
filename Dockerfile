FROM python:3.7

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
  sudo \
  cmake \
  python3-setuptools &&\
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* &&\
  pip --no-cache-dir install \
  googletrans 