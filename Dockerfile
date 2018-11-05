FROM        ubuntu:18.04
MAINTAINER  dev.younlab@gmail.com

ENV         BUILD_MODE  dev
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

#build commend
#sudo docker build -t [tag:tag] -f Dockerfile .

#run commend
#docker run --rm -it -p 7000:8000 [tag:tag]

#ubuntu setup
RUN     apt -y update
RUN     apt -y dist-upgrade
RUN     apt -y install python3-pip

# server module install
RUN     apt -y install nginx
RUN     pip3 install uwsgi
RUN     apt -y install supervisor

COPY    requirements.txt    /tmp/
RUN     pip3 install -r     /tmp/requirements.txt

#projects dir copy
COPY    ./  /srv/project

RUN     rm -rf /etc/nginx/sites-available/*
RUN     rm -rf /etc/nginx/sites-enabled/*

RUN     cp -f /srv/project/.config/app.nginx \
              /etc/nginx/sites-available/app.nginx
RUN     cp -f /srv/project/.config/supervisor.conf \
              /etc/supervisor/conf.d/supervisor.conf

#RUN     cp -f /srv/project/.config/nginx.conf \
#              /etc/nginx/nginx.conf

RUN     ln -sf /etc/nginx/sites-available/app.nginx \
               /etc/nginx/sites-enabled/app.nginx

#run commend
WORKDIR /srv/project/app

RUN     python3 manage.py collectstatic --noinput
#RUN     uwsgi --http :8000 --chdir /srv/project/app --wsgi config.wsgi
#is local server
#CMD     python3 manage.py runserver 0:8000

EXPOSE      80

CMD     supervisord -n
