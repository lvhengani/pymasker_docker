# This docker is based on ubuntu 16:04
# The objective is to download MODIS collection 6 with this docker

FROM ubuntu:16.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GOSU_VERSION=1.9

RUN sed 's/main$/main universe multiverse/' -i /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
        build-essential \
        python \
        python-dev \
        python-distribute \
        python-pip \
        software-properties-common && \
    add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
    apt-get install -y \
        gdal-bin \
        libgdal-dev \
        python-gdal \
        python-pyproj \
        python-numpy \
        python-scipy \
        curl && \
    pip install pymasker && \    
    pip install --upgrade pip && \
    curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64" && \
    chmod +x /usr/local/bin/gosu 
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
