FROM thinkwhere/gdal-python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /duan
WORKDIR /duan

COPY requirements.txt /duan/
RUN pip install -r requirements.txt 

COPY . /duan/
ADD ./attach/custom_geo_field /usr/local/lib/python3.6/site-packages/django/contrib/gis/templates/gis/admin/custom_geo_field