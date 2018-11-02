FROM        ubuntu:18.04
MAINTAINER  dev.younlab@gmail.com

#ubuntu setup
RUN     apt -y update
RUN     apt -y dist-upgrade
RUN     apt -y install python3-pip

# server module install
RUN     apt -y install nginx
RUN     pip3 install uwsgi

#projects dir copy
COPY    .  /srv/project
WORKDIR /srv/project
RUN     pip3 install -r requirements.txt

#run commend
ENV     export DJANGO_SETTINGS_MODULE=config.settings.dev
WORKDIR /srv/project/app

CMD     python3 manage.py runserver 0:8000
