#! /bin/bash
service mysql start $ sleep 10

debconf-set-selections <<< "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2"  
debconf-set-selections <<< "phpmyadmin phpmyadmin/dbconfig-install boolean true"  
debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/admin-user string admin"  
debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/admin-pass password arshad956"  
debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/app-pass password arshad956"  
debconf-set-selections <<< "phpmyadmin phpmyadmin/app-password-confirm password arshad956"

apt-get -y install phpmyadmin



