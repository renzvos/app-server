<?php

class Production {
	public $prod = false;
	public $host;
	public $user;
	public $password;
	public $database;
	public $appsfolder;
	public $selfapi;
	public $analyticsapi;
	public $geolocationapi;
	public $paymentsapi;
	public $backupapi;
	public $phptimezone;


function __construct()
{
	
	if($this->prod == true)
	{
		$this->host = "localhost";
		$this->user = "root";
		$this->password = "arshad956";
		$this->database = "rex";
		$this->selfapi = "http://34.66.158.177/otpserver/development/api/";
		$this->analyticsapi = "http://vacuolar-load.000webhostapp.com/api/";
		$this->geolocationapi = "https://geolocation-db.com/json/";
		$this->paymentsapi = "https://payments.renzvos.com";
		$this->backupapi = "http://10.128.0.10/api/";
		$this->appsfolder =  "/var/www/html/otpserver/production/Apps";
		$this->phptimezone = "UTC";
		date_default_timezone_set($this->phptimezone);
	}
	else
	{
		$this->host = "localhost";
		$this->user = "root";
		$this->password = "";
		$this->database = "rex";
		$this->selfapi = "http://localhost/findlon/server/development/api/";
		$this->analyticsapi = "http://localhost/analytics/api/";
		$this->geolocationapi = "https://geolocation-db.com/json/";
		$this->paymentsapi = "http://localhost/payments/index.php";
		$this->backupapi = "http://localhost/backup/api/";
		$this->appsfolder =  "D:/Works/rex-server/api/clients/dependency";
		$this->phptimezone = "Asia/Kolkata";
		date_default_timezone_set($this->phptimezone);
	}

}

}


?>