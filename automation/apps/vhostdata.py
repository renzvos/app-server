

def vhostdata(name,alias,location):
    data = '''<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerName '''+ name + '''
	ServerAlias ''' + alias + '''
	ServerAdmin webmaster@localhost
	DocumentRoot ''' + location +  '''

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf

</VirtualHost>
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet


    '''
    return data


def vhostssl(name,alias,location,certificate,key):
	data = '''
	<IfModule mod_ssl.c>
		<VirtualHost *:443>
			# The ServerName directive sets the request scheme, hostname and port that
			# the server uses to identify itself. This is used when creating
			# redirection URLs. In the context of virtual hosts, the ServerName
			# specifies what hostname must appear in the request's Host: header to
			# match this virtual host. For the default virtual host (this file) this
			# value is not decisive as it is used as a last resort host regardless.
			# However, you must set it for any further virtual host explicitly.

			ServerName '''+ name + '''
			ServerAlias ''' + alias + '''
			ServerAdmin webmaster@localhost
			DocumentRoot ''' + location +  '''

			# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
			# error, crit, alert, emerg.
			# It is also possible to configure the loglevel for particular
			# modules, e.g.
			#LogLevel info ssl:warn

			ErrorLog ${APACHE_LOG_DIR}/error.log
			CustomLog ${APACHE_LOG_DIR}/access.log combined

			# For most configuration files from conf-available/, which are
			# enabled or disabled at a global level, it is possible to
			# include a line for only one particular virtual host. For example the
			# following line enables the CGI configuration for this host only
			# after it has been globally disabled with "a2disconf".
			#Include conf-available/serve-cgi-bin.conf

			SSLEngine on
			SSLProtocol             all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1
			SSLCipherSuite          ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
			SSLHonorCipherOrder     off
			SSLSessionTickets       off
			SSLOptions +StrictRequire
			SSLCertificateFile '''+ certificate + '''
			SSLCertificateKeyFile '''+ key + '''

		</VirtualHost>
	</IfModule>
	'''

	return data
    