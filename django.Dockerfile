FROM python:3.6.8-jessie

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apt-get update -y \
    && apt-get upgrade -y\
    && apt-get install software-properties-common -y\
    && add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main"\
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add -\
    && apt-get update\
    && apt-get install postgresql-9.6 postgresql-client-9.6 postgresql-contrib-9.6 -y\
    && apt-get install -y  locales \
    && apt-get install -y gdal-bin python-gdal python3-gdal \
    && apt-get update && apt-get install -y gettext libgettextpo-dev \
    # Cleanup
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/