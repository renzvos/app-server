FROM ubuntu:18.04

RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install git -y

RUN apt-get install python3 -y
RUN apt-get install python3-distutils -y
RUN apt-get install python3-apt -y
RUN apt install python3-pip -y --upgrade
RUN apt install python-pip -y --upgrade
RUN apt-get install -y python-dev
RUN apt install python3 python3-venv libaugeas0 -y



RUN apt-get -y install  apache2
RUN apt install lsb-release ca-certificates apt-transport-https software-properties-common -y
RUN add-apt-repository ppa:ondrej/php

RUN apt install php8.0 libapache2-mod-php8.0 -y
RUN service apache2 restart

RUN apt install php8.0-cli php8.0-common php8.0-imap php8.0-redis php8.0-snmp php8.0-xml -y
RUN apt install php8.0-mysql -y


RUN apt-get -y install libc6
RUN apt-get -y install libglapi-mesa
RUN apt-get -y install libxdamage1
RUN apt-get -y install libxfixes3
RUN apt-get -y install libxcb-glx0
RUN apt-get -y install libxcb-dri2-0
RUN apt-get -y install libxcb-dri3-0
RUN apt-get -y install libxcb-present0
RUN apt-get -y install libxcb-sync1
RUN apt-get -y install libxshmfence1
RUN apt-get -y install libxxf86vm1
RUN apt-get -y install php-curl





RUN python3 -m venv /opt/certbot/
RUN /opt/certbot/bin/pip install --upgrade pip
RUN /opt/certbot/bin/pip install certbot certbot-apache
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot

RUN apt-get install mysql-client -y


RUN rm -rf /var/www/html





#Cache stops
COPY automation automation
COPY config config
RUN python3 config/setconfig.py

RUN a2enmod headers
RUN service apache2 start

EXPOSE 80:80
EXPOSE 443:443
ENTRYPOINT ["/usr/bin/python3","automation/start.py"] 