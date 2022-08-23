# GDAL python
# FROM python:3.6-stretch as python-gdal

# # Update base container install
# RUN apt-get update
# RUN apt-get upgrade -y

# # Add unstable repo to allow us to access latest GDAL builds
# RUN echo deb http://ftp.uk.debian.org/debian unstable main contrib non-free >> /etc/apt/sources.list
# RUN apt-get update

# # Existing binutils causes a dependency conflict, correct version will be installed when GDAL gets intalled
# RUN apt-get remove -y binutils

# # Install GDAL dependencies
# RUN apt-get -t unstable install -y libgdal-dev g++

# # Update C env vars so compiler can find gdal
# ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
# ENV C_INCLUDE_PATH=/usr/include/gdal

# # This will install GDAL 2.3.2
# RUN pip install GDAL==2.3.2

# # Project python
# FROM python-gdal as project-python
# FROM mypython:v1


FROM thinkwhere/gdal-python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /duan
WORKDIR /duan

COPY requirements_prod.txt /duan/
RUN pip install -r requirements_prod.txt 

COPY . /duan/
ADD ./attach/custom_geo_field /usr/local/lib/python3.6/site-packages/django/contrib/gis/templates/gis/admin/custom_geo_field